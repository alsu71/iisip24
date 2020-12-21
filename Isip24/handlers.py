# Import library
from main import bot, dp
from aiogram import types
from aiogram.types import Message

arrayKeyboard = ["🧠","Item2","Вопросы","Подкаты"]
arrayKeyboard1 = ["Сколько планет в солнечной системе?", "Знаешь ли ты ...", "Какой твой куратор?"]

keyboard_markup = types.ReplyKeyboardMarkup(row_width=3)

arrayTackles = ["Я конечно не Путин, но глядя на тебя я состарился", "Мне сказали, что я могу к тебе подкатить, но у меня нет тачки,бэйб", " Я конечно не Among Us , но для тебя я буду предателем"]
arrayShelf = ["🧠","Item2","Вопросы","Подкаты"]

arrayShelf1 = ["Хороший","Плохой","Лучший","Хуже только я"]

arrayQuestion = ["Сколько планет в солнечной системе?", "Знаешь ли ты ...", "Какой твой куратор?"]

# Send message to admin
async def send_to_admin(dp):
        await bot.send_message(chat_id=1043917541, text="Bot start")
        
# Start bot using func
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    text = f'''Привет! {message.from_user.full_name}
Получается это бот 🤖
🙌 Для работы бота в группе необходимо дать ему права администратора и включить все разрешения .
Бот создан при поддержки ФИО'''
    keyboard_markup.add(*(types.KeyboardButton(text) for text in arrayKeyboard))
    await message.answer(text=text, reply_markup=keyboard_markup)
    
    
@dp.message_handler()
async def all_message(message: types.Message):
    if message.text == "Item2":
        await message.answer(text="Вы нажали на Item 2 👩🏽‍🦰 и ничего не произошло. Поздравляю, ты лох! ")
    if message.text == "Дурак":
        await message.answer(text="Сам дурак 🧠")
    if message.text == "🧠":
        await message.answer(text="Кто проживает на дне океана?")
    if message.text == "Спанч Боб":
        await message.answer(text="Так ты губка рванные штаны!")
    if message.text == "Подкаты":
    	await message.answer(text="")
    if message.text == "Вопросы":
    	await message.answer(random.choice(arrayQuestion))
    if message.text == "8 планет":
    	await message.answer("Ты молодец! Возьми с полки пирожок и кусочек масла. Адрес: Наглая улица, дом Охреневший, квартира Идилесом")
    if message.text == "9 планет":
    	await message.answer("Ты "очень умный", но ты не справился. Ведь теперь планет 8,а не 9. Плутон это ты!")
    if message.text == "Иди нахер":
    	await message.answer("Посмотрите кто тут ротик открыл, сейчас муха залетит!")
    if message.text == "вдоль ночных дорог":
    	await message.answer("Шла босиком ...")
    if message.text == "не жалея ног":
    	await message.answer("(смайлик музыки)")  
    if message.text == "Какой твой куратор?":
    	await message.answer(keyboard_markup.add(*(types.KeyboardButton(text) for text in arrayKeyboard1))
    await message.answer(text=text, reply_markup=keyboard_markup))
    if message.text == "Хороший":
    	await message.answer("А мог быть еще лучше!")
    if message.text == "Плохой":
    	await message.answer("Заведи нового.")
    if message.text == "Лучший":
    	await message.answer("THE BEST ONLY IN RUSSIA")
    if message.text == "Хуже только я":
    	await message.answer("Какая ирония. На пары просто надо приходить!!!")
