
from aiogram.filters import Command
from aiogram import Router, types, F 
# from bot import dp
# from bot.keyboards.keyboard import main_menu_keyboard
from bot.keyboards.keyboard import main_menu_keyboard, inline_destination_keyboard
from aiogram.types import CallbackQuery
from bot.keyboards.keyboard import inline_destination_keyboard
# from aiogram.filters import Command, F

message_router = Router()

@message_router.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer("Welcome to the Discover Ethiopia Bot! Use /explore to begin your journey.", reply_markup=main_menu_keyboard())


@message_router.message(Command('explore'))
async def cmd_explore(message: types.Message):
    

    # Edit the message to replace the reply keyboard with the inline keyboard
    inline_keyboard = inline_destination_keyboard()
    await message.answer("Choose a destination to explore:", reply_markup=inline_keyboard)
   





