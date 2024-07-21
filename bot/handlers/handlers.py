from aiogram import Router, F, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message, ReplyKeyboardRemove

from bot.handlers.keyboard_button import (
    WALLET,
    DEPOSIT,
    RATING,
    REFERRAL_PROGRAM,
    CREATE, GET, SEND, EXCHANGE, STARTMENU,
    KWEI, MWEI, GWEI, MICROETHER, ETHER,
    DAO_IN_USDC, REQUEST_USDC,
    DAO_IN_W3, REQUEST_W3,
    DAO_FROM_W3_TO_USDT, REQUEST_W3_USDT
)
from bot.handlers.states import SixCode, Transaction, DAOTRANSITION


router = Router()


@router.message(F.text == STARTMENU)
@router.message(CommandStart())
async def command_start(
    message: types.Message,
) -> None:
    await message.answer(
        'Hi! what do you want?',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=WALLET),
                    KeyboardButton(text=DEPOSIT),
                    KeyboardButton(text=RATING),
                    KeyboardButton(text=REFERRAL_PROGRAM),
                ]
            ],
        ),
    )
