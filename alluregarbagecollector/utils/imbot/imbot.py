"""
Инициализация бота для VK Teams
"""

from bot.bot import Bot

from utils.config.config import configuration


imbot = Bot(**configuration["vk_team_bot"])
