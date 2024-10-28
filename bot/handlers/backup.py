from os.path import join
from time import sleep

import os
import subprocess

from aiogram import Router, types, F, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ContentType, ParseMode
from aiogram.filters import Command
from aiogram.types import FSInputFile

from bot.dispacher import TOKEN

routine = Router()

media_handlers = {
    ContentType.PHOTO: lambda message: message.answer_photo(message.photo[-1].file_id,
                                                            caption="Siz yuborgan rasm qaytmoqda!"),
    ContentType.VIDEO: lambda message: message.answer_video(message.video.file_id,
                                                            caption="Siz yuborgan video qaytmoqda!"),
    ContentType.AUDIO: lambda message: message.answer_audio(message.audio.file_id,
                                                            caption="Siz yuborgan audio qaytmoqda!"),
    ContentType.VOICE: lambda message: message.answer_voice(message.voice.file_id,
                                                            caption="Siz yuborgan ovoz qaytmoqda!"),
    ContentType.DOCUMENT: lambda message: message.answer_document(message.document.file_id,
                                                                  caption="Siz yuborgan hujjat qaytmoqda!"),
}


@routine.message(F.content_type.in_(
    [ContentType.PHOTO, ContentType.VIDEO, ContentType.AUDIO, ContentType.VOICE, ContentType.DOCUMENT]))
async def handle_media(message: types.Message):
    handler = media_handlers.get(message.content_type)
    if handler:
        await handler(message)


async def send_doc(bot: Bot, my_id, path):
    file = FSInputFile(join(path), "backupfile.tar")
    await bot.send_document(chat_id=my_id, document=file)


@routine.message(Command(commands=["backup"]))
async def backup(message: types.Message):
    await message.answer("Starting backup process...")
    await message.answer("FAQAT DOCKER COMPOSE BILAN ISHLAYDI")
    await message.answer("FAQAT DOCKER COMPOSE BILAN ISHLAYDI")
    bash_script_path = r'/app/backup_script.sh'
    bash_script_content = """
    BACKUP_DIR='/app/backup'
    FILE_NAME=$BACKUP_DIR/$(date +'%d-%m-%Y-%H-%M-%S').tar
    PGPASSWORD='1'
    docker exec -e PGPASSWORD=$PGPASSWORD pg pg_dump -U postgres -h localhost -p 5432 -d idk -F tar -f /tmp/db_backup.tar
    docker cp pg:/tmp/db_backup.tar $FILE_NAME
    echo $FILE_NAME
    """
    with open(bash_script_path, 'w') as file:
        file.write(bash_script_content)
    os.chmod(bash_script_path, 0o755)
    try:
        result = subprocess.run(
            ['/bin/bash', bash_script_path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        output = result.stdout.decode('utf-8').strip()
        error_output = result.stderr.decode('utf-8')

        if output:
            backup_file_path = output
            await message.answer(f"Backup completed successfully! File: {backup_file_path}")
            bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
            my_id = message.from_user.id
            await send_doc(bot, my_id, backup_file_path)

        if error_output:
            await message.answer(f"Errors: {error_output}")

    except subprocess.CalledProcessError as e:
        await message.answer(f"An error occurred during the backup process: {e.stderr.decode('utf-8')}")
