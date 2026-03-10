import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✈️ Aviator Simulator Bot\n\nType /play to simulate a round."
    )

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    crash = round(random.uniform(1.1, 10.0), 2)
    await update.message.reply_text(f"🚀 Plane crashed at {crash}x")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("play", play))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
