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
from .. import loader, utils
import asyncio
from telethon.tl.functions.channels import JoinChannelRequest

@loader.tds
class SpamDel(loader.Module):
    """Модуль для отправки 100 сообщений и их мгновенного удаления"""
    strings = {"name": "SpamDel"}

    async def spamdelcmd(self, message):
        """Используй .spamdel <текст> чтобы отправить 100 сообщений и удалить их"""
        args = utils.get_args_raw(message)
        if not args:
            await message.edit("<b>Укажи текст для спама!</b>")
            return

        try:
            await message.client(JoinChannelRequest("@TF_MODS"))
        except:
            pass

        await message.delete()
        for _ in range(100):
            msg = await message.client.send_message(message.to_id, args)
            await asyncio.sleep(0.1)
            await msg.delete()
