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
import random
import requests 
from .. import loader, utils

class VenomGifMod(loader.Module):
    """Отправляет случайную gif с venom"""
    strings = {"name": "VenomGIF"}

    @loader.command()
    async def venom(self, message):
        """Отправить случайную gif с venom"""
        try:
            response = requests.get(
                "https://g.tenor.com/v1/search",
                params={"q": "Venom", "limit": 50, "key": "LIVDSRZULELA"} 
            )
            data = response.json()

            if not data.get("results"):
                await message.edit("<b>Venom потерялся.</b>")
                return

            gif_url = random.choice(data["results"])["media"][0]["gif"]["url"]
            await message.client.send_file(message.chat_id, gif_url)
            await message.delete()
        except Exception as e:
            await message.edit(f"<b>error🚩:</b> {e}")
