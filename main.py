from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5954796922:AAFmCQxqfe8Ybb1oBkwkG6c2x6eu4BF7UJs").build() 

app.add_handler(CommandHandler("hello", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("MoonAge", MoonAge_command))
app.add_handler(CommandHandler("timetoNY", TimeToNY_command))
app.add_handler(CommandHandler("anekdot", anekdot_command))

print('Сервер запущен')
app.run_polling()





