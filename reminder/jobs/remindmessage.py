from datetime import datetime, timedelta
import os

from linebot import LineBotApi
from linebot.models import TextSendMessage, FlexSendMessage

from flask import current_app, logging
from reminder.models.schedule import Schedule, ScheduleSchema
from reminder.service.messageservice import MessageService


logger = logging.create_logger(current_app)
# 環境変数取得
CHANNEL_ACCESS_TOKEN = os.environ["CHANNEL_ACCESS_TOKEN"]

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def remind_message():
    time_now = datetime.now().replace(microsecond=0).replace(second=0) + timedelta(hours=9)
    logger.info(f"reminds start. time now => {time_now}")
    remind_schedules = Schedule.get_by_time(time_now)
    schedule_schema = ScheduleSchema(many=True)
    message_service = MessageService()
    remind_msgs_list = message_service.create_reminds_from_list(schedule_schema.dump(remind_schedules))

    remind_count = 0
    for user_id, msgs in remind_msgs_list.items():
        for msg in msgs:
            messages = FlexSendMessage(alt_text=msg["body"]["contents"][0]["text"], contents=msg)
            line_bot_api.push_message(user_id, messages=messages)
            remind_count += 1
    logger.info(f"reminds done. total count => {remind_count}")

    delete_count = Schedule.delete_by_time(time_now)
    logger.info(f"delete done. total count => {delete_count}")