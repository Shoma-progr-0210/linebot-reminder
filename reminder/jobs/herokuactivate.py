import requests

def heroku_activate():
    requests.get('https://line-bot-echo-202101301430.herokuapp.com/activate')