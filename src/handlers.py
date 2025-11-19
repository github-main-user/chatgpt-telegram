from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup

from src.llm import answer_message, clear_dialog

router = Router()
keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Новый запрос")]], resize_keyboard=True
)


@router.message(Command("start"))
async def cmd_start(message: Message):
    clear_dialog(message.from_user.id)  # type: ignore
    await message.answer("UwU", reply_markup=keyboard)


@router.message(F.text == "Новый запрос")
async def cmd_clear_dialog(message: Message):
    clear_dialog(message.from_user.id)  # type: ignore
    await message.answer("Контекст диалога сброшен", reply_markup=keyboard)


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("UwU")


@router.message()
async def cmd_answer_user(message: Message):
    if not message.text:
        return

    answer = await answer_message(message.from_user.id, message.text)  # type: ignore
    await message.answer(
        answer if answer is not None else "Model provided an empty answer",
        reply_markup=keyboard,
    )
