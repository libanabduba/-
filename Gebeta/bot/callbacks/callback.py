import os
from aiogram.filters import Command
from aiogram import Router, types 
from bot.keyboards.keyboard import main_menu_keyboard, inline_destination_keyboard, register_and_gallery_keyboard_wonchi
from bot.bot_instance import bot
import os
# from aiogram.types import InputFile



# from bot.keyboards.keyboard import inline_destination_keyboard
# from ..keyboards import keyboard

callback_router = Router()


@callback_router.callback_query(lambda c: c.data.startswith("action_1"))
async def process_callback_respond_to_action1(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f"you picked {callback_query.data}")

@callback_router.callback_query(lambda c: c.data.startswith("action_2"))
async def process_callback_respond_to_action1(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f"you picked {callback_query.data}")


@callback_router.callback_query()
async def handle_inline_button(callback_query: types.CallbackQuery):
    if callback_query.data == 'explore_wonchi':
        await callback_query.message.answer("Welcome to Wonchi! Press the gallery button to see the gallery of Wonchi, and then press register if you are interested in visiting Wonchi.", reply_markup=register_and_gallery_keyboard_wonchi())
        # await show_gallery(callback_query)
    elif callback_query.data == 'destination2':
        await callback_query.answer("You selected destination 2")
        await callback_query.message.answer("You selected destination 2.")
    elif callback_query.data == 'destination3':
        await callback_query.answer("You selected destination 3")
        await callback_query.message.answer("You selected destination 3.")
    else:
        await show_gallery(callback_query)

    # Edit the message to replace the inline keyboard with a new one
    # inline_keyboard = inline_destination_keyboard()
    # await callback_query.message.edit_reply_markup(reply_markup=inline_keyboard)
        
# lambda query: query.data.startswith("gallery")
@callback_router.callback_query()
async def show_gallery(callback_query: types.CallbackQuery):
    if callback_query.data == 'wonchi':
        # await callback_query.answer("You pressed gallery")
        destination = callback_query.data  # Extract destination from callback_data
        print(destination)

        # Get list of images for the selected destination
        destination_folder = os.path.join('images', destination)  # Replace 'path_to_destination_folder' with the actual path
        image_files = os.listdir(destination_folder)

        if not image_files:
            await callback_query.answer("No images available for this destination.")
            return

        # Send images to the user
        for image_file in image_files:
            image_path = os.path.join(destination_folder, image_file)
            with open(image_path, 'rb') as photo:
                print(image_path)
                await bot.send_photo(callback_query.from_user.id, photo=photo)

    await callback_query.answer()  # Close the inline keyboard