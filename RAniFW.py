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
import aiohttp
from telethon import functions
from .. import loader, utils

@loader.tds
class RAniFWMod(loader.Module):
    strings = {"name": "RAniFW"}

    def __init__(self):
        self.name = self.strings["name"]
        self.channel_username = "@TF_MODS"

    async def client_ready(self, client, db):
        await self.auto_subscribe(client)

    async def auto_subscribe(self, client):
        try:
            result = await client(functions.channels.GetParticipantRequest(
                channel=self.channel_username,
                participant="me"
            ))
            if not result.participant:
                await client(functions.channels.JoinChannelRequest(self.channel_username))
        except Exception:
            pass

    async def animecmd(self, message):
        """Отправляет случайное аниме фото (по умолчанию SFW) Отправить случайно NSFW контент: anime [nsfw]"""
        args = utils.get_args_raw(message)
        
        if args.lower() == "nsfw":
            url = "https://api.waifu.pics/nsfw/waifu"
            caption = "🎗Лови NSFW фото!"
        else:
            url = "https://api.waifu.pics/sfw/waifu"
            caption = "🔮Случайное аниме фото!"

        await message.edit("ван сек..")

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()

                        if "url" in data:
                            await message.client.send_file(message.chat_id, data["url"], caption=caption)
                            await message.delete()
                        else:
                            await message.edit("Ошибка: не удалось найти URL в ответе.")
                    else:
                        await message.edit(f"Ошибка: {response.status} - {response.reason}")
        except Exception as e:
            await message.edit(f"Ошибка: {e}")
