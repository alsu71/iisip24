import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram import Bot, Dispatcher, executor
import csv, datetime, pymysql


API_TOKEN = '1403015492:AAF5RnUmzD_Uy9BRpmRYpe2TkjlgjqXquDs'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.reply("Привет!")
    statistics(message.chat.id, message.text, message.from_user.username)
    stat(message.chat.id, message.text)

def stat(user_id, command):
    connection = pymysql.connect('194.58.103.48', 'aiogramstat', 'nik10101976', 'aiogramstat')
    cursor = connection.cursor()
    data = datetime.datetime.today().strftime("%Y-%m-%d %H:%M")
    cursor.execute("INSERT INTO stat(user_id, user_command, date) VALUS ('%s', '%s', '%s')" % (user_id, command, data))
    connection.commit()
    cursor.close()
    
if __name__ == '__main__':
    executor.start_polling(dp)