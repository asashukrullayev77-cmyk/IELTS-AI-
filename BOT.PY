import os
import logging
import asyncio
from aiogram import Bot, Dispatcher, html, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

# Telegram bot tokenini Railway Environment Variables (Atrof-muhit o'zgaruvchilari)dan oladi
TOKEN = os.getenv("BOT_TOKEN")

# Loglarni sozlash (Xatoliklarni kuzatish uchun)
logging.basicConfig(level=logging.INFO)

# Bot va Dispatcher obyektlarini yaratish
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Bosh menyu tugmalari
def get_main_keyboard():
    kb = [
        [KeyboardButton(text="🎧 Listening"), KeyboardButton(text="📖 Reading")],
        [KeyboardButton(text="✍️ Writing"), KeyboardButton(text="🗣️ Speaking")],
        [KeyboardButton(text="📊 Mening natijalarim")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

# /start komandasi uchun handler
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    # Foydalanuvchi ismini olish (username bo'lmasa, full_name olinadi)
    user_name = message.from_user.username
    display_name = f"@{user_name}" if user_name else message.from_user.full_name
    
    welcome_text = (
        f"Salom {html.bold(display_name)}! 👋\n\n"
        f"IELTS imtihoniga tayyorgarlik ko'rish botiga xush kelibsiz.\n"
        f"Bu yerda siz xuddi {html.code('ieltsgg')} platformasidagi kabi 4 ta ko'nikma bo'yicha test topshirishingiz mumkin.\n\n"
        f"Tayyor bo'lsangiz, quyidagi menyudan kerakli bo'limni tanlang 👇"
    )
    await message.answer(welcome_text, parse_mode="HTML", reply_markup=get_main_keyboard())

# Listening bo'limi
@dp.message(F.text == "🎧 Listening")
async def listening_handler(message: Message):
    text = (
        "🎧 *Listening bo'limi*\n\n"
        "Bu bo'limda sizga audio fayl va unga tegishli savollar taqdim etiladi.\n"
        "Hozirda testlar bazasi yangilanmoqda. Tez orada to'liq testlar qo'shiladi!"
    )
    await message.answer(text, parse_mode="Markdown")

# Reading bo'limi
@dp.message(F.text == "📖 Reading")
async def reading_handler(message: Message):
    text = (
        "📖 *Reading bo'limi*\n\n"
        "Bu bo'limda siz matnlarni o'qib, 40 ta savolga javob berishingiz kerak bo'ladi.\n"
        "Yaqin soatlarda ilk akademik matnlar yuklanadi!"
    )
    await message.answer(text, parse_mode="Markdown")

# Writing bo'limi
@dp.message(F.text == "✍️ Writing")
async def writing_handler(message: Message):
    text = (
        "✍️ *Writing bo'limi*\n\n"
        "Task 1 va Task 2 mavzulari shu yerda aks etadi.\n"
        "Inshongizni yozib yuborganingizdan so'ng, u AI yoki mutaxassis tomonidan tekshiriladi."
    )
    await message.answer(text, parse_mode="Markdown")

# Speaking bo'limi
@dp.message(F.text == "🗣️ Speaking")
async def speaking_handler(message: Message):
    text = (
        "🗣️ *Speaking bo'limi*\n\n"
        "Part 1, Part 2 va Part 3 savollariga ovozli xabar (Voice message) orqali javob bering.\n"
        "Tizim ovozingizni yozib olib, tahlil qiladi."
    )
    await message.answer(text, parse_mode="Markdown")

# Natijalar bo'limi
@dp.message(F.text == "📊 Mening natijalarim")
async def stats_handler(message: Message):
    await message.answer("📊 Siz hali birorta ham test topshirmadingiz. Natijalar shu yerda yig'iladi.")

# Botni ishga tushirish funksiyasi
async def main() -> None:
    logging.info("Bot muvaffaqiyatli ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
