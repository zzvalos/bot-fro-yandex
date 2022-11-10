из  случайного  выбора импорта 

импорт  telebot

токен  = "

telebot = бот.TeleBot(токен)


= RANDOM_TASKS ['Написать Гвидо письмо', 'Выучить Python', 'Записаться на курс в Нетологию', 'Посмотреть 4 сезон Рик и Морти']

dict = todos()


СПРАВКА  = "'
Список доступных команд:
* print - напечать все задачи на заданную дату
* todo - добавить задачу
* random - добавить на сегодня случайную задачу
* help - Напечатать help
'''


add_todo  определение (дата, задача):
    дата = дата.ниже()
    задача  if.get(дата)  не  является None:
        задачи [дата].добавить(задача)
    ещё:
        задачи[дата] = [задача]


@bot.message_handler(команды=['help'])
help  def(сообщение):
    бот.отправить_сообщение(message.chat.id , ПОМОГИТЕ)


@bot.message_handler(commands=['random'])
def random(message):
    task = choice(RANDOM_TASKS)
    add_todo('сегодня', task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на сегодня')


@bot.message_handler(commands=['add'])
def add(message):
    _, date, tail = message.text.split(maxsplit=2)
    task = ' '.join([tail])
    add_todo(date, task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {date}')


@bot.message_handler(commands=['show'])
def print_(message):
    date = message.text.split()[1].lower()
    if date in todos:
        tasks = ''
        for task in todos[date]:
            tasks += f'[ ] {task}\n'
    else:
        tasks = 'Такой даты нет'
    bot.send_message(message.chat.id, tasks)


bot.polling(none_stop=True)
