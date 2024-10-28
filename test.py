# from telethon import TelegramClient, events
#
# # Replace 'api_id' and 'api_hash' with your own values
# api_id = '22440443'
# api_hash = '8a7c4abf24fb71a092bd72da73e3865f'
# phone = '+998880505502'
#
# # Create the client and connect
# client = TelegramClient('new_session_name', api_id, api_hash)
#
#
# # Function to send an automated reply
# @client.on(events.NewMessage(incoming=True))
# async def handler(event):
#     sender = await event.get_sender()
#     # Check if it's a personal message (not a group or channel)
#     if event.is_private:
#         await event.reply("Hey, I'm currently away. I'll get back to you as soon as I can!")
#
#
# # Start the client
# with client:
#     client.run_until_disconnected()
# import asyncio
# from db import db, Base  # Import your db instance and Base
# from db.models import Product, User
#
#
# # Import your models to ensure they are registered with Base.metadata
#
# async def init_db():
#     db.init()  # Initialize the connection to the database
#
#     # Check if engine is initialized
#     if db._engine is None:
#         print("Engine was not initialized. Please check the connection settings.")
#         return
#
#     # Enable SQL logging
#     db._engine.echo = True
#
#     try:
#         # Using the engine connection inside an async context manager
#         async with db._engine.connect() as conn:
#             print("Database connection successful!")
#     except Exception as e:
#         print(f"Database connection failed: {e}")
#         return  # Exit if connection fails
#
#     # Explicitly creating tables within a transaction
#     async with db._engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#         print("Tables created successfully!")
#
#
# def main1():
#     asyncio.run(init_db())
#     print("Database initialization completed.")
#
#
# if __name__ == "__main__":
#
#     # If this script is executed directly, run the main function
#     main1()

#
# import os
# import re
#
#
# # Kommentariyani o'chiruvchi funksiya
# def remove_comments_from_file(file_path):
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
#
#     # Kommentariyalarni o'chirish uchun yangi fayl yarating
#     with open(file_path, 'w') as file:
#         for line in lines:
#             # Kommentariyalarni topish va o'chirish
#             line_without_comment = re.sub(r'#', ' ', line).rstrip()
#             if line_without_comment.strip():  # Faqat bo'sh bo'lmagan satrlarni yozamiz
#                 file.write(line_without_comment + '\n')
#
#
# # Loyihangizdagi barcha Python fayllarni ko'rib chiqish
# def remove_comments_from_project(directory):
#     for foldername, subfolders, filenames in os.walk(directory):
#         for filename in filenames:
#             if filename.endswith('.py'):  # Faqat .py fayllarni ko'rib chiqish
#                 file_path = os.path.join(foldername, filename)
#                 remove_comments_from_file(file_path)
#
#
# # Loyihangiz papkasiga yo'l ko'rsating
# project_directory = 'C:/Users/User/PycharmProjects/XOLODILNIK'
# remove_comments_from_project(project_directory)
#


# from apscheduler.schedulers.blocking import BlockingScheduler
# import backup_maker
#
# db_name = 'idk'
# user = 'postgres'
# password = '1'
# host = 'localhost'
# port = 5432
# backup_dir = 'backup'
# scheduler = BlockingScheduler()
#
# scheduler.add_job(
#     backup_maker.backup_postgres_db,
#     'interval',
#     hours=24,
#     args=[db_name, user, password, host, port, backup_dir]
# )
#
# try:
#     scheduler.start()
# except (KeyboardInterrupt, SystemExit):
#     pass
# Sample data for users
# from alembic import context
# print(dir(context))  # List all available attributes
#
# try:
#     config = context.config
#     print("Config loaded successfully")
# except AttributeError:
#     print("Error: 'config' attribute not found in alembic context.")
# from aiogram import Bot, Dispatcher, types
# import os
#
# TOKEN = '7518997294:AAFg3JC5aJnf7k74luL16tLymuBunXHzFbM'
# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)
#
#
# @dp.message(commands=['backup'])
# async def backup(message: types.Message):
#     backup_dir = "C:\\Users\\User\\PycharmProjects\\XOLODILNIK\\backup"
#     file_name = f"{backup_dir}\\backup_{datetime.now().strftime('%d-%m-%Y-%H-%M-%S')}.tar"
#     os.system(f"PGPASSWORD='1' docker exec pg pg_dump -U postgres -h localhost -p 5432 -d idk -F tar -f {file_name}")
#     await message.answer(f"Backup created: {file_name}")
#
#
# if __name__ == "__main__":
#     from aiogram import executor
#     from datetime import datetime
#
#     executor.start_polling(dp)



# import subprocess
#
# # Path to the PowerShell script
# ps_script_path = r'C:\Users\User\PycharmProjects\XOLODILNIK\backup_script.ps1'
#
# # PowerShell script content
# ps_script_content = """
# $BACKUP_DIR = 'C:\\Users\\User\\PycharmProjects\\XOLODILNIK\\backup'
# $FILE_NAME = $BACKUP_DIR + '\\' + (Get-Date -Format 'dd-MM-yyyy-hh-mm-ss') + '.tar'
# $PGPASSWORD = '1'
# docker exec -e PGPASSWORD=$PGPASSWORD pg pg_dump -U postgres -h localhost -p 5432 -d idk -F tar -f '/tmp/db_backup.tar'
# docker cp pg:/tmp/db_backup.tar $FILE_NAME
# """
#
# # Write the content to the .ps1 file
# with open(ps_script_path, 'w') as file:
#     file.write(ps_script_content)
#
# # Execute the PowerShell script
# try:
#     result = subprocess.run(
#         ['powershell', '-File', ps_script_path],
#         check=True,
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE
#     )
#     output = result.stdout.decode('utf-8')
#     error_output = result.stderr.decode('utf-8')
#
#     print("Script executed successfully!")
#     if output:
#         print("Output:", output)
#     if error_output:
#         print("Errors:", error_output)
#
# except subprocess.CalledProcessError as e:
#     print("Error occurred while executing the script")
#     print("Error output:", e.stderr.decode('utf-8'))


from PIL import Image

# Load the image
image_path = "img.png"
img = Image.open(image_path)

# Resize the image to smaller dimensions (let's say 320x180 for this case)
new_size = (640, 360)
img_resized = img.resize(new_size)

# Save the resized image to a valid path on your local system
resized_image_path = "C:\\Users\\User\\PycharmProjects\\XOLODILNIK\\aa.png"
img_resized.save(resized_image_path)

print(f"Image saved at {resized_image_path}")
