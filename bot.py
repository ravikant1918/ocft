# create  atyelegram bot that continus pull message from bot and if get then reply 

import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from app import JobSeeker 

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
js = JobSeeker()

# Function to handle incoming messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update)
    user_message = update.message.text
    chat_id = update.message.chat_id
    mobile = js.call_prospeo_mobile_finder(linkedin_url=user_message)
    print(f"Received message from {chat_id}: {user_message}")
    # Reply to the message
    await context.bot.send_message(chat_id=chat_id, text=f"User mobile number is : {mobile}")

# Create and run the bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # Add handler to catch all text messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("Bot is running...")
    app.run_polling()
