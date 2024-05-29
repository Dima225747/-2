import logging
from telebot import TeleBot

logging.basicConfig(level=logging.INFO)

bot = TeleBot("7152832160:AAEBxNtpUsNIUZjHIAnSoDXL8H1kHjiRJGs")


def get_child_progress(child_name):
    progress_data = {
        "Шлегель": {
            "Математика": "4",
            "Английский язык": "3",
            "История": "5",
            "Основы профессионльной деятельности": "Незачёт"
        },
        "Тарасов": {
            "Математика": "5",
            "Английский язык": "Отсутствует",
            "История": "Моя история ещё не закончилась"
        }
    }

    return progress_data.get(child_name, {})


@bot.message_handler(commands=['start', 'help'])
def process_start_command(message):
    bot.reply_to(message, "Привет! Я бот для просмотра успеваемости вашего ребенка. Для просмотра успеваемости введите /успеваемость <фамилию ребенка>.")


@bot.message_handler(commands=['успеваемость'])
def process_progress_command(message):
    if len(message.text.split()) > 1:
        child_name = message.text.split()[1]
        progress_data = get_child_progress(child_name)
        if progress_data:
            progress_info = "\n".join([f"{subject}: {grade}" for subject, grade in progress_data.items()])
            bot.reply_to(message, f"Успеваемость ученика {child_name}:\n{progress_info}")
        else:
            bot.reply_to(message, f"Информация об успеваемости ученика {child_name} не найдена.")
    else:
        bot.reply_to(message, "Пожалуйста, укажите фамилию ученика после команды /успеваемость.")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Я не понимаю ваш запрос. Для просмотра успеваемости введите /успеваемость <фамилию ребенка>.")


if __name__ == "__main__":
    bot.polling()




