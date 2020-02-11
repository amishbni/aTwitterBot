from telegram.ext import Updater, CommandHandler
from config import BOT_TOKEN

def start(update, context):
    bot = context.bot
    chat_id = update.effective_chat.id

    bot.send_message(chat_id=chat_id, text="Hello, World!")

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
