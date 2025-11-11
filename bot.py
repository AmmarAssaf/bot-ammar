import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# إعداد التسجيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """يرسل رسالة ترحيب عندما يتم إرسال الأمر /start"""
    user = update.message.from_user
    await update.message.reply_text(
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

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """يعرض رسالة المساعدة"""
    await update.message.reply_text(
        '📋 **أوامر البوت:**\n\n'
        '/start - بدء استخدام البوت\n'
        '/help - عرض هذه الرسالة\n'
        '/info - معلومات عن البوت\n\n'
        '🔧 البوت يعمل بنجاح على Render!'
    )

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """يعرض معلومات عن البوت"""
    await update.message.reply_text(
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
        # إنشاء التطبيق
        application = Application.builder().token(BOT_TOKEN).build()
        
        # إضافة معالجات الأوامر
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CommandHandler("info", info))
        application.add_handler(CommandHandler("مساعدة", help_command))
        application.add_handler(CommandHandler("معلومات", info))
        
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
        application.run_polling()
        
    except Exception as e:
        logger.error(f"❌ خطأ في تشغيل البوت: {e}")

if __name__ == '__main__':
    main()
