from aiogram.filters import Command
from aiogram import Router, types 
from aiogram.utils.keyboard import InlineKeyboardBuilder


# from bot.keyboards.keyboard import inline_destination_keyboard
from ..keyboards import keyboard

callback_router = Router()


@callback_router.callback_query(lambda c: c.data.startswith("action_1"))
async def process_callback_respond_to_action1(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f"you picked {callback_query.data}")

@callback_router.callback_query(lambda c: c.data.startswith("action_2"))
async def process_callback_respond_to_action1(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f"you picked {callback_query.data}")


@callback_router.callback_query()
async def process_explore(callback_query: types.CallbackQuery):
    from bot.keyboards.keyboard import register_and_gallery_keyboard
   
    # # Send a welcome message to the selected destination
    # welcome_message = f"Welcome to {destination}! How would you like to explore?"
    # await callback_query.message.edit_text(welcome_message, reply_markup=main_menu_keyboard())

    # # Provide additional options with inline buttons
    # options_keyboard = InlineKeyboardMarkup()
    # options_keyboard.row(
    #     InlineKeyboardButton("Gallery", callback_data=f"gallery_{destination.lower().replace(' ', '_')}"),
    #     InlineKeyboardButton("Other Option 1", callback_data=f"other_option_1_{destination.lower().replace(' ', '_')}"),
    #     InlineKeyboardButton("Other Option 2", callback_data=f"other_option_2_{destination.lower().replace(' ', '_')}")
    # )

    if callback_query.data == "explore_wonchi":
        await callback_query.message.answer("Welcome to Wonchi", reply_markup=keyboard.register_and_gallery_keyboard)