# meta developer: @TF_MODS
"""
                       ___         ___           ___          _____          ___
      ___        /  /\       /__/\         /  /\        /  /::\        /  /\
     /  /\      /  /:/_     |  |::\       /  /::\      /  /:/\:\      /  /:/_
    /  /:/     /  /:/ /\    |  |:|:\     /  /:/\:\    /  /:/  \:\    /  /:/ /\
   /  /:/     /  /:/ /:/  __|__|:|\:\   /  /:/  \:\  /__/:/ \__\:|  /  /:/ /::\
  /  /::\    /__/:/ /:/  /__/::::| \:\ /__/:/ \__\:\ \  \:\ /  /:/ /__/:/ /:/\:\
 /__/:/\:\   \  \:\/:/   \  \:\~~\__\/ \  \:\ /  /:/  \  \:\  /:/  \  \:\/:/~/:/
 \__\/  \:\   \  \::/     \  \:\        \  \:\  /:/    \  \:\/:/    \  \::/ /:/
      \  \:\   \  \:\      \  \:\        \  \:\/:/      \  \::/      \__\/ /:/
       \__\/    \  \:\      \  \:\        \  \::/        \__\/         /__/:/
                 \__\/       \__\/         \__\/
"""
import asyncio
from datetime import datetime
import pytz
from telethon.tl.functions.account import UpdateProfileRequest

from .. import loader, utils

@loader.tds
class TimeInNickMod(loader.Module):
    """модуль транслирующий время в вашем нике"""
    strings = {"name": "TimeInNick"}

    def __init__(self):
        self.running = False
        self.timezone = 'Europe/Moscow'

    async def client_ready(self, client, db):
        self.client = client
        self.db = db

    async def timenickcmd(self, message):
        """Включить/выключить временя в нике"""
        if self.running:
            self.running = False
            await message.edit("<b>❎время в вашем nickname успешно выключено</b>")
        else:
            self.running = True
            await message.edit("<b>✅время в вашем nickname успешно включено!</b>")
            self.client.loop.create_task(self.update_nick())

    async def time_mskcmd(self, message):
        """Переключить время на МСК"""
        self.timezone = 'Europe/Moscow'
        await message.edit("<b>🔨успешно изменен часовой пояс на MOSCOW</b>")
    
    async def time_ekbcmd(self, message):
        """Переключить время на ЕКB"""
        self.timezone = 'Asia/Yekaterinburg'
        await message.edit("<b>🧱успешно изменен часовой пояс на EKB</b>")
        
    async def time_omskcmd(self, message):
        """Переключить время в нике на OMSK"""
        self.timezone='Asia/Omsk'
        await message.edit("<b>🔧успешно изменен часовой пояс на OMSK</b>")
    
    async def time_samaracmd(self, message):
        """Переключить время на САМАРА"""
        self.timezone='Europe/Samara'
        await message.edit("<b>🪛успешно изменен часовой пояс на SAMARA</b>")
    
    async def update_nick(self):
        while self.running:
          
            tz = pytz.timezone(self.timezone)
            current_time = datetime.now(tz).strftime("%H:%M")
            
            double_struck_time = self.to_double_struck(current_time)
            double_struck_bar = "𝕀" 

            me = await self.client.get_me()
            current_nick = me.first_name.split('𝕀')[0].strip()
            
            new_nick = f"{current_nick} {double_struck_bar} {double_struck_time}"
            try:
                await self.client(UpdateProfileRequest(first_name=new_nick))
            except Exception as e:
                print(f"📡что-то пошло не так..: {e}")
            
            now = datetime.now()
            sleep_time = 60 - now.second
            await asyncio.sleep(sleep_time)

    def to_double_struck(self, text):
        normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        double_struck = "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡"
        translation = str.maketrans(normal, double_struck)
        return text.translate(translation)
