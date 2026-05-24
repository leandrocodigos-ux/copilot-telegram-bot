"""Main entry point for the Copilot Telegram Bot."""

import asyncio
import logging
from config import FLASK_HOST, FLASK_PORT, LOG_LEVEL
from server.api import create_app
from bot.telegram_bot import TelegramBot

# Configure logging
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def main():
    """Main application entry point."""
    logger.info("Starting Copilot Telegram Bot...")
    
    # Initialize Flask app
    flask_app = create_app()
    logger.info(f"Flask app created (Host: {FLASK_HOST}, Port: {FLASK_PORT})")
    
    # Initialize Telegram bot
    telegram_bot = TelegramBot()
    logger.info("Telegram bot initialized")
    
    # Start the bot
    await telegram_bot.start()
    logger.info("Telegram bot started")
    
    # Run Flask server in a separate thread
    from threading import Thread
    flask_thread = Thread(target=lambda: flask_app.run(
        host=FLASK_HOST, 
        port=FLASK_PORT, 
        debug=False
    ), daemon=True)
    flask_thread.start()
    logger.info("Flask server started")
    
    try:
        logger.info("Bot is running. Press Ctrl+C to stop.")
        # Keep the bot running
        await asyncio.Event().wait()
    except KeyboardInterrupt:
        logger.info("Shutting down...")
        await telegram_bot.stop()
        logger.info("Bot stopped")


if __name__ == '__main__':
    asyncio.run(main())