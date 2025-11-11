import os
import logging
from telegram.ext import Application, CommandHandler

# إعداد مبسط
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update, context):
    await update.message.reply_text('🎉 البوت يعمل بنجاح! السلام عليكم')

def main():
    BOT_TOKEN = os.getenv('BOT_TOKEN', '8415474087:AAEDtwjvgogXfvpMzARe875svIEkSSDdNXk')
    
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    logger.info("🚀 البوت يعمل!")
    app.run_polling()

if __name__ == '__main__':
    main()
