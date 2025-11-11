import os
import logging
from telegram.ext import Application, CommandHandler

# إعداد التسجيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update, context):
    """يرسل رسالة ترحيب عندما يتم إرسال الأمر /start"""
    user = update.message.from_user
    await update.message.reply_text(
        f'السلام عليكم ورحمة الله وبركاته 🌟\n\n'
        f'أهلاً بك {user.first_name}!\n\n'
        '✅ البوت يعمل بنجاح على Render\n'
        '🚀 تم حل جميع المشاكل التقنية\n'
        '🎉 يمكنك الآن تطوير البوت كما تريد'
    )

async def hello(update, context):
    """يرد على المستخدم بكلمة السلام عليكم"""
    await update.message.reply_text('وعليكم السلام ورحمة الله وبركاته 🌸')

def main():
    logger.info("🚀 بدء تشغيل البوت المبسط...")
    
    # الحصول على التوكن من متغير البيئة
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    
    if not BOT_TOKEN:
        logger.error("❌ BOT_TOKEN غير موجود في متغيرات البيئة")
        return
    
    try:
        # إنشاء التطبيق
        application = Application.builder().token(BOT_TOKEN).build()
        
        # إضافة معالجات الأوامر
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("hello", hello))
        application.add_handler(CommandHandler("السلام", hello))
        application.add_handler(CommandHandler("اهلا", hello))
        
        logger.info("✅ البوت المبسط جاهز للعمل!")
        print("=" * 50)
        print("🤖 البوت يعمل بنجاح!")
        print("💡 جرب هذه الأوامر:")
        print("   /start - بدء البوت")
        print("   /hello - إلقاء التحية")
        print("   /السلام - إلقاء التحية")
        print("=" * 50)
        
        # بدء البوت
        application.run_polling()
        
    except Exception as e:
        logger.error(f"❌ خطأ في تشغيل البوت: {e}")

if __name__ == '__main__':
    main()
