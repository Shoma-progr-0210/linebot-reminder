from flask import Flask, request, abort
import psycopg2
import os
from datetime import datetime, timedelta
import traceback
import requests
import json

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    FollowEvent, UnfollowEvent, MessageEvent, PostbackEvent,
    TextMessage, TextSendMessage, FlexSendMessage, TemplateSendMessage,
    ButtonsTemplate, CarouselTemplate, CarouselColumn,
    PostbackTemplateAction
)

from reminder.app import app
from reminder.models.schedule import Schedule, ScheduleSchema
from reminder.service.messageservice import MessageService


# 環境変数取得
CHANNEL_ACCESS_TOKEN = os.environ["CHANNEL_ACCESS_TOKEN"]
CHANNEL_SECRET = os.environ["CHANNEL_SECRET"]
# DB_HOST = os.environ["DB_HOST"]
# DB_PORT = os.environ["DB_PORT"]
# DB_DBNAME = os.environ["DB_DBNAME"]
# DB_USER = os.environ["DB_USER"]
# DB_PASSWORD = os.environ["DB_PASSWORD"]

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', os.environ["LIFF_URL"])
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response


@app.route("/")
def hello_world():
    return "hello world!"

@app.route("/activate")
def hi():
    return "OK"

@app.route("/register", methods=['POST'])
def register():
    # body = json.loads(request.get_data())
    json_data = request.get_json()
    # data = json.loads(json_data)
    app.logger.info(json_data)

    return 'OK'


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg_from = event.message.text
    reply_msg = ""
    if msg_from == "ヘルプ" or msg_from == "help":
        # ヘルプメニュー
        reply_msg = "メニュー:\n" \
        + "(なし) => オウム返し\n" \
        + "登録 => リマインドの登録を行います。フォーマットは以下です。\n" \
            + "登録\n" \
            + "<予定名>\n" \
            + "<時間(例：2021/2/7 23:38)>\n" \
            + "<ラベル名>\n" \
            + "<メッセージ>\n"
    elif msg_from.startswith("登録\n"):
        # 登録
        # 予定名
        # 時間: %Y/%m/%d %H:%M
        # ラベル
        # メッセージ
        try:
            profile = line_bot_api.get_profile(event.source.user_id)
            app.logger.info(f"user profile => {profile}")
            data = msg_from.split("\n")
            name = data[1]
            message = data[4]
            time = datetime.strptime(data[2], '%Y/%m/%d %H:%M')
            label = data[3]
            result = Schedule.create(profile.user_id, name, message, time, label)
            app.logger.info(f"create => {result}")

            reply_msg = "リマインドを登録しました。"
        except:
            app.logger.warning(traceback.format_exc())
            reply_msg = "リマインドの登録に失敗しました。"
    elif msg_from.startswith("予定一覧"):
        profile = line_bot_api.get_profile(event.source.user_id)
        schedules = Schedule.get_by_user_id(profile.user_id)
        if schedules:
            schedule_schema = ScheduleSchema(many=True)
            message_service = MessageService()
            # jsonがlist型になるので、str型に変換
            carousel = message_service.create_carousel_from_list(schedule_schema.dump(schedules))
            app.logger.info(carousel)
            line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text='予定一覧',
                    contents=carousel
                )
            )
        else:
            reply_msg = "登録された予定はありません"
    else:
        # それ以外はオウム返し
        reply_msg = msg_from

    if reply_msg:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_msg)
        )

# FlexMessageのボタン押下
@handler.add(PostbackEvent)
def on_postback(event):
    postback_msg = event.postback.data
    user_id = event.source.user_id
    if postback_msg == 'edit':
        line_bot_api.push_message(
            to=user_id,
            messages=TextSendMessage(text='編集が押下されました')
        )
    elif postback_msg == 'check':
        line_bot_api.push_message(
            to=user_id,
            messages=TextSendMessage(text='確認が押下されました')
        )

if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)