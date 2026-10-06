import os
from telegram import InlineKeyboardButton as B, InlineKeyboardMarkup as M
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

def menu():
    return M([
        [B("🤝 Создать сделку", "new"), B("🛍 Услуги", "services")],
        [B("💼 Партнёры", "partners"), B("📊 Мои сделки", "deals")],
        [B("📋 Условия", "rules"), B("💬 Поддержка", "support")],
        [B("ℹ️ О сервисе", "about")]
    ])

async def start(update, context):
    await update.message.reply_text(
        "🖤 WINNELY GRAM\n\n"
        "Безопасные сделки • Услуги • Партнёры\n\n"
        "Выберите нужный раздел:",
        reply_markup=menu()
    )

async def click(update, context):
    q = update.callback_query
    await q.answer()

    texts = {
        "new": "🤝 СОЗДАНИЕ СДЕЛКИ\n\nВыберите роль:\n\n🛒 Покупатель\n📦 Продавец",
        "services": "🛍 УСЛУГИ\n\n🎨 Дизайн\n📱 Telegram\n💻 Разработка\n📢 Реклама\n🔧 Другое",
        "partners": "💼 ПАРТНЁРЫ\n\nПриглашайте клиентов и получайте вознаграждение.",
        "deals": "📊 МОИ СДЕЛКИ\n\nЗдесь будут отображаться ваши активные и завершённые сделки.",
        "rules": "📋 УСЛОВИЯ\n\nВсе участники подтверждают условия сделки перед её проведением.",
        "support": "💬 ПОДДЕРЖКА\n\nОпишите проблему — поддержка поможет.",
        "about": "ℹ️ WINNELY GRAM\n\nПлатформа для безопасных сделок, услуг и партнёрства."
    }

    await q.edit_message_text(
        texts.get(q.data, "WINNELY GRAM"),
        reply_markup=M([[B("⬅️ Главное меню", "back")]])
    )

async def back(update, context):
    q = update.callback_query
    await q.answer()
    await q.edit_message_text(
        "🖤 WINNELY GRAM\n\nВыберите нужный раздел:",
        reply_markup=menu()
    )

token = os.getenv("BOT_TOKEN")
if not token:
    raise RuntimeError("BOT_TOKEN не задан")

app = Application.builder().token(token).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(back, pattern="^back$"))
app.add_handler(CallbackQueryHandler(click))
app.run_polling()
