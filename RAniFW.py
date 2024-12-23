# Лицензия TF_MODS
LICENSE_TEXT = """
TF_MODS - Лицензия

Данная лицензия предоставляет вам право использовать, копировать, изменять и распространять данный файл при соблюдении следующих условий:
1. **Использование**: Вы можете использовать, копировать или распространять данный файл только в рамках законодательства, применимого в вашей юрисдикции.
2. **Изменения**: Вы можете изменять данный файл в рамках ваших нужд, однако все изменения должны быть четко обозначены и документированы.
3. **Отказ от ответственности**: Данный файл предоставляется "как есть", без каких-либо гарантий. Мы не несем ответственности за любые убытки или повреждения, которые могут возникнуть при использовании или модификации этого файла.
4. **Ссылки на оригинал**: Если вы распространяете модификации или форки этого файла, вы должны указать, что это основано на оригинальной версии файла TFMODS.
5. **Не для коммерческого использования**: Если не указано иное, данный файл и его модификации не могут быть использованы в коммерческих целях без разрешения владельцев прав.
Настоящая лицензия распространяется на все содержимое данного файла, включая, но не ограничиваясь, текстами, кодом, и изображениями.
6. **Некоторые модули дорабатываются CHATGPT, но НИКАК не копируются чужие модули.(если такое всё же произошло свяжитесь со мной в комментариях)

#meta developer: @TF_MODS
"""

import aiohttp
from .. import loader, utils

@loader.tds
class RAniFWMod(loader.Module):
    strings = {"name": "RAniFW"}

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
