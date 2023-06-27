import telebot
from telebot import types

TOKEN = 'TOKEN'
main_channel_ids = [-idchanel, -idchanel] # Список id Основных каналов
extra_channel_ids = [-idchanel, -idchanel]  # Список id дополнительных каналов

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)


# Обработчик новых сообщений
@bot.channel_post_handler(content_types=['text', 'photo', 'video', 'document'])
def handle_message(message):
    if message.chat.id in main_channel_ids:
        # Проверяем, содержит ли текст хэштег "#реклама"
        if not ('#реклама' in (message.caption or '') or '#реклама' in (message.text or '')):
            # Копируем текст сообщения
            text = message.caption or message.text or ''

            # Отправляем сообщение в каждый дополнительный канал
            for extra_channel_id in extra_channel_ids:
                if message.photo:
                    media = message.photo[-1].file_id
                    bot.send_photo(extra_channel_id, media, caption=text)
                elif message.video:
                    media = message.video.file_id
                    bot.send_video(extra_channel_id, media, caption=text)
                elif message.document:
                    media = message.document.file_id
                    bot.send_document(extra_channel_id, media, caption=text)
                elif text:
                    bot.send_message(extra_channel_id, text)

            print('Сообщение успешно скопировано и отправлено в дополнительные каналы')


# Запускаем бота
bot.polling()