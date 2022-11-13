import os
from dotenv import load_dotenv, find_dotenv

# Loading .env variables
load_dotenv(find_dotenv())

TELEGRAM_TOKEN = "5617623078:AAG_pk36IhLnHouYk42wq7WmM1jC3iAgw24"
if TELEGRAM_TOKEN is None:
    raise Exception("Please setup the .env variable TELEGRAM_TOKEN.")

PORT = int(os.environ.get('PORT', '8443'))
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")

TELEGRAM_SUPPORT_CHAT_ID = "423468963"
if TELEGRAM_SUPPORT_CHAT_ID is None or not str(TELEGRAM_SUPPORT_CHAT_ID).lstrip("-").isdigit():
    raise Exception("You need to specify 'TELEGRAM_SUPPORT_CHAT_ID' env variable: The bot will forward all messages to this chat_id. Add this bot https://t.me/ShowJsonBot to your private chat to find its chat_id.")
TELEGRAM_SUPPORT_CHAT_ID = int(TELEGRAM_SUPPORT_CHAT_ID)


WELCOME_MESSAGE = "WELCOME BRO"
REPLY_TO_THIS_MESSAGE = "User above don't allow forward his messages. Reply to this message"
WRONG_REPLY = "Wrong reply"