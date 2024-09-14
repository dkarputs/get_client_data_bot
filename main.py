import asyncio
import logging
from aiogram.filters.command import Command
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from aiogram import Bot, Dispatcher, types

logging.basicConfig(level=logging.INFO)

Base = declarative_base()


class User(Base):
    __tablename__ = 'audience'

    id = Column(Integer, primary_key=True)
    pixel_id = Column(String)
    username = Column(String)
    user_id = Column(String)
    chat_id = Column(String)
    channel_name = Column(String)
    campaign_name = Column(String)
    campaign_id = Column(String)
    adset_id = Column(String)
    adset_name = Column(String)
    ad_id = Column(String)
    ad_name = Column(String)
    placement = Column(String)
    site_source_name = Column(String)


bot = Bot(token="7369957883:AAFEc1jBYVTTJxd6NPb_ffCCZzIxZrP0Mzs")
dp = Dispatcher()

trusted_users = [
    6938328370,
    5977247440,
    6791807705,
    7045147070,
    7004043574,
    6520393044,
    792280460
]


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    if message.from_user.id not in trusted_users:
        return None
    await message.answer(
        "Привет! Я бот для работы с базой данных. Пришли мне id пользователя, чтобы получить данные о нем.")


@dp.message()
async def get_data(message: types.Message):
    user_id = message.text
    user = db_session.query(User).filter_by(user_id=user_id).first()
    if user is None:
        await message.answer("Пользователь не найден.")
    else:
        await message.answer(f"ID пользователя: {user.user_id}\n"
                             f"Имя пользователя: {user.username}\n"
                             f"ID канала: {user.chat_id}\n"
                             f"Название канала: {user.channel_name}\n"
                             f"ID кампании: {user.campaign_id}\n"
                             f"Название кампании: {user.campaign_name}\n"
                             f"ID адсета: {user.adset_id}\n"
                             f"Название адсета: {user.adset_name}\n"
                             f"ID объявления: {user.ad_id}\n"
                             f"Название объявления: {user.ad_name}\n"
                             f"Размещение: {user.placement}\n"
                             f"Источник сайта: {user.site_source_name}\n"
                             f"Pixel ID: {user.pixel_id}\n")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    engine = create_engine('postgresql://postgres:postgres@vpn-vds113.eleos.tk:5432/postgres')
    Session = sessionmaker(bind=engine)
    db_session = Session()
    asyncio.run(main())
