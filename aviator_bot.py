# aviator_bot.py
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Get the token from environment variable
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN environment variable not set!")

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎮 Aviator Simulator Bot\n\n"
        "Use /play to simulate a round."
    )

# Simulate a game round
import random

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    crash_point = round(random.uniform(1.1, 10.0), 2)
    await update.message.reply_text(f"🚀 Round result: CRASH = {crash_point}x")

# Main function
def main():
    # Create bot application
    app = ApplicationBuilder().token(TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("play", play))

    # Run bot
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
