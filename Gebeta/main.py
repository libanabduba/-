import asyncio 

from aiogram import Dispatcher

from bot.bot_instance import bot
from bot.handlers.message_handler import message_router
from bot.callbacks.callback import callback_router


def register_routers(dp: Dispatcher) -> None:
    """Registers routers"""

    dp.include_router(message_router)

    # callback routers
    dp.include_router(callback_router)





async def main() -> None:
    """The main function which will execute our event loop and start polling."""
    try:
        dp = Dispatcher()

        print('Bot Starting....')
        register_routers(dp)
        print("Polling ....")
        
        # Increase the timeout period for the HTTP client
        # session = dp.bot.session
        # session.connector._ssl_handshake_timeout = 30

        await dp.start_polling(bot)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    

if __name__ == "__main__":
    asyncio.run(main())