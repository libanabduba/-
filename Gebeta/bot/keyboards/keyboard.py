from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton



def main_menu_keyboard():
    main_menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[])
     # Creating a list of buttons
    buttons = [
        [KeyboardButton(text="Explore Destinations")],
        [KeyboardButton(text="Travel Tips")],
        [KeyboardButton(text="My Favorites")]
    ]

    # Adding the list of buttons to the keyboard
    for button in buttons:
        main_menu.keyboard.append(button)

    return main_menu

def help_menu_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[])
    keyboard.add(KeyboardButton("Help"))
    keyboard.add(KeyboardButton("Contact Support"))
    keyboard.add(KeyboardButton("Back to Main Menu"))
    return keyboard

def inline_destination_keyboard():
    

    keyboard = InlineKeyboardMarkup(inline_keyboard= [
         [InlineKeyboardButton(text="Wonchi",  callback_data="explore_wonchi"),InlineKeyboardButton(text="Koysha",  callback_data="explore_koysha")],
        [InlineKeyboardButton(text="Cebera Curcura",  callback_data="explore_Cbera"),InlineKeyboardButton(text="Halal Kela",  callback_data="explore_Halal")],
        [InlineKeyboardButton(text="Gorgora",callback_data="explore_Halal")]
    ], resize_keyboard=True, one_time_keyboard=True)

    # for button in destinations:
    #     keyboard.inline_keyboard.append(button)
    
    return keyboard

def back_to_main_menu_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[])
    keyboard.add(KeyboardButton("Back to Main Menu"))
    return keyboard

def register_and_gallery_keyboard_wonchi():
    keyboard = InlineKeyboardMarkup(inline_keyboard= [
         [InlineKeyboardButton(text="gallery",  callback_data="wonchi"),InlineKeyboardButton(text="register",  callback_data="register")],
       
    ])
    
    return keyboard
