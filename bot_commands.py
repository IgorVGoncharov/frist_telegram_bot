from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
import random

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    #await update.message.reply_text(f'Привет {update.effective_user.first_name}')
    await update.message.reply_text(f'Привет {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Что я умею:\n/hello - говорю привет!\n\
/time - показываю текущее время\n/help - оказываю помощь\n\
/sum - суммирую числа А числа B (/sum A B). \n\
/MoonAge - определяю возраст луны\n\
/timetoNY - показываю сколько осталось до нового года\n\
/anekdot - выдаю разные анекдоты')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{str(datetime.datetime.now().time())[:8]}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mess = update.message.text
    items = mess.split()
    a = int(items[1])
    b = int(items[2])
    await update.message.reply_text(a+b)

async def TimeToNY_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    now = str((datetime.datetime.now().date()))
    day = int(now[8:10])
    month = int(now[5:7])
    val = 31-day
    if val == 1 or val == 21:
        day = 'День'
    elif (val >= 2 and val <=4) or (val >= 22 and val <= 24):
        day = 'Дня'
    else:
        day = 'Дней'
    await update.message.reply_text(f'До нового года осталось: {val} {day} и {12-month} месяцев')

async def MoonAge_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    now = str((datetime.datetime.now().date()))
    day = int(now[8:10])
    month = int(now[5:7])
    year = int(now[0:4])
    L = year - 2012
    W = L*11 -14 + day + month 
    while W > 30:
        W -= 30
    if (W >= 0 and W < 7) or W == 30:
        await update.message.reply_text(f'Возраст Луны (дней) - {W}. Новолуние. Луна не видна.')
    elif (W >= 7 and W < 15):
        await update.message.reply_text(f'Возраст Луны (дней) - {W}. Первая четверть. Наилучшее время для наблюдений – вечер.')
    elif (W >= 15 and W < 22):
        await update.message.reply_text(f'Возраст Луны (дней) - {W}. Полнолуние. Видна всю ночь от заката до восхода Солнца.')   
    elif W(W >= 22 and W < 30):
        await update.message.reply_text(f'Возраст Луны (дней) - {W}. Последняя четверть. Луну лучше наблюдать во второй половине ночи, под утро.')

async def anekdot_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    list = []
    already = []
    with open('anekdot.txt', 'r', encoding='utf8') as data:
        list = data.read()
    list = list.split('***')
    index = random.randint(0, len(list))
    await update.message.reply_text(list[index])