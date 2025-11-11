from telegram.ext import Application, CommandHandler
import os
import logging

# إعداد التسجيل
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

async def start(update, context):
    await update.message.reply_text('مرحباً! البوت يعمل الآن 🎉')

async def help_command(update, context):
    await update.message.reply_text('الأوامر المتاحة:\n/start - بدء التشغيل\n/help - المساعدة')

def main():
    try:
        application = Application.builder().token(TOKEN).build()
        
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        
        logger.info("🚀 البوت يعمل...")
        application.run_polling()
    except Exception as e:
        logger.error(f"❌ خطأ: {e}")

if __name__ == '__main__':
    main()
