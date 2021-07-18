from flask_apscheduler import APScheduler
from reminder.jobs.remindmessage import remind_message
from reminder.jobs.herokuactivate import heroku_activate


class Config(object):
    SCHEDULER_API_ENABLED = True

scheduler = APScheduler()

# リマインド
@scheduler.task('cron', id='remind_job', minute='*')
def remind_job():
    app = scheduler.app
    with app.app_context():
        app.logger.info('This remind job is run every a minute.')
        remind_message()

# herokuのスリープ防止
@scheduler.task('cron', id='activate_job', minute='*/15')
def activate_job():
    app = scheduler.app
    with app.app_context():
        app.logger.info('This activate job is run every 15 minutes.')
        heroku_activate()

def scheduler_start(app):
    app.config.from_object(Config())
    # scheduler.api_enabled = True
    scheduler.init_app(app)
    scheduler.start()