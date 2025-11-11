import os
import logging
from telegram.ext import Updater, CommandHandler

# إعداد التسجيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def start(update, context):
    """يرسل رسالة ترحيب عندما يتم إرسال الأمر /start"""
    user = update.message.from_user
    update.message.reply_text(
        f'السلام عليكم ورحمة الله وبركاته 🌟\n\n'
        f'أهلاً بك {user.first_name}!\n\n'
        '✅ البوت يعمل بنجاح على Render\n'
        '🚀 تم حل جميع المشاكل التقنية\n'
        '🎉 يمكنك الآن تطوير البوت كما تريد\n\n'
        '💡 الأوامر المتاحة:\n'
        '/start - بدء البوت\n'
        '/help - المساعدة\n'
        '/info - معلومات عن البوت'
    )

def help_command(update, context):
    """يعرض رسالة المساعدة"""
    update.message.reply_text(
        '📋 **أوامر البوت:**\n\n'
        '/start - بدء استخدام البوت\n'
        '/help - عرض هذه الرسالة\n'
        '/info - معلومات عن البوت\n\n'
        '🔧 البوت يعمل بنجاح على Render!'
    )

def info(update, context):
    """يعرض معلومات عن البوت"""
    update.message.reply_text(
        '🤖 **معلومات البوت:**\n\n'
        '• الإسم: بوت التلغرام الأساسي\n'
        '• المنصة: Render\n'
        '• الحالة: ✅ يعمل بشكل ممتاز\n'
        '• الإصدار: 1.0\n\n'
        '🎉 تم حل جميع المشاكل التقنية!'
    )

def main():
    """الدالة الرئيسية لتشغيل البوت"""
    logger.info("🚀 بدء تشغيل البوت...")
    
    # الحصول على التوكن من متغير البيئة
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    
    if not BOT_TOKEN:
        logger.error("❌ BOT_TOKEN غير موجود في متغيرات البيئة")
        return
    
    try:
        # إنشاء التطبيق (لإصدار 13.15)
        updater = Updater(BOT_TOKEN, use_context=True)
        dispatcher = updater.dispatcher
        
        # إضافة معالجات الأوامر
        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(CommandHandler("help", help_command))
        dispatcher.add_handler(CommandHandler("info", info))
        dispatcher.add_handler(CommandHandler("مساعدة", help_command))
        dispatcher.add_handler(CommandHandler("معلومات", info))
        
        logger.info("✅ البوت جاهز للعمل!")
        print("=" * 50)
        print("🤖 البوت يعمل بنجاح!")
        print("📍 مستضاف على: Render")
        print("💡 الأوامر المتاحة:")
        print("   /start - بدء البوت")
        print("   /help - المساعدة") 
        print("   /info - معلومات البوت")
        print("=" * 50)
        
        # بدء البوت
        updater.start_polling()
        updater.idle()
        
    except Exception as e:
        logger.error(f"❌ خطأ في تشغيل البوت: {e}")

if __name__ == '__main__':
    main()
