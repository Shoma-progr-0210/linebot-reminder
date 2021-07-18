from flask import Flask
import os
import logging
from flask_cors import CORS

from reminder.database import init_db
import reminder.models


app = Flask(__name__)

# レベルの変更
app.logger.setLevel(logging.INFO)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DB_URL"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
with app.app_context():
    # CORS(app)
    init_db(app)
    # リマインドスケジュール起動
    from reminder.schedule import scheduler_start
    scheduler_start(app)
