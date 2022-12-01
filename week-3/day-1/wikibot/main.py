import logging

from aiogram import Bot, Dispatcher, executor, types

import wikipedia

wikipedia.set_lang('uz')

API_TOKEN = '5316136617:AAFQykQEy7xZ4GVan_vEQ_h_I8Ywsg3ubFI'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Salom Wikibotga Xush kelibsiz!")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Bu bot Wikipedia dan foydali ma'lumotlarni olib jo'natadi!")


@dp.message_handler()
async def wiki(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    try:
        response = wikipedia.summary(message.text)
        if len(response) >= 4000:
            for i in range(0, len(response), 4000):
                await message.answer(response[i:i + 4000])
        else:
            await message.answer(response)
    except:
        await message.answer('Bu mavzuga oid maqola topilmadi!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
