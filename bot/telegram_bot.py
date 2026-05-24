"""Telegram Bot integration module."""

from telegram.ext import Application
from config import TELEGRAM_TOKEN


class TelegramBot:
    """Main Telegram Bot class."""
    
    def __init__(self):
        """Initialize the Telegram bot."""
        self.application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    async def start(self):
        """Start the bot."""
        await self.application.initialize()
        await self.application.start()
    
    async def stop(self):
        """Stop the bot."""
        await self.application.stop()
        await self.application.shutdown()