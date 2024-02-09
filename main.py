from telebot import types
import telebot
import requests
TOKEN_BOT = '6890700789:AAHlj0GjOGxjNfKctMwB-cLiDf90VYObA8I'
bot = telebot.TeleBot(TOKEN_BOT)

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text ='''Приветствую пользователь, Московский зоопарк предлогает всем желающиим пройти викторину "Моё тотемное животное"
    Для начала викторнины нажмите /quize
    info: Данный бот создан с целью привлечения внимания к проекту "Возьми животное под опеку" 
    Для более подробной информации об этом проекте нажмите: /info'''
    bot.send_message(message.chat.id,text)

@bot.message_handler(commands=['info'])
def info(message: telebot.types.Message):
    text = '''Программа "Возьми животное под опеку" существует для улучшения условий содержания животных.
     По этой программе любой человек может стать опекуном животного, за несущественную ежемесячную плау.
     Опекун может в любое время дня узнавать как чувствует себя опекаемое животное, и приходить проведовать его.
     Если заинтересовало обратись на почту Semensokolov2206@icloud.com 
     Чтобы вернуться к викторине нажми /quize'''
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands= ['quize' ])
def quize(message: telebot.types.Message):
   text = '''Добро пожаловать в викторину
   А вот и твой первый вопрос: 
   Где бы ты хотел жить?:
    /forest🌲 лес
    /jungle🌳  джунгли
    /savannah🌴 саванна
    '''
   bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['forest'])#лесное животное
def forest(message: telebot.types.Message):
    text = '''Отлично, ты выбрал лес!
    А вот и следующий вопрос: 
    Какую еду ты больше любишь?
    /meat1   мясо 
    /grass1  зелень 
    '''
    bot.send_message(message.chat.id, text)
@bot.message_handler(commands=['jungle'])#животное из джунглей
def jungle(message: telebot.types.Message):
    text = '''Отлично, ты выбрал джунгли! 
     А вот и следующий вопрос: 
    Какую еду ты больше любишь?
    /meat2   мясо
    /grass2  растительная пища'''
    bot.send_message(message.chat.id, text)
@bot.message_handler(commands=['savannah'])#животное из саванны
def savannah(message: telebot.types.Message):
    text = '''Отлично, ты выбрал саванну!
    А вот и следующий вопрос: 
    Какую еду ты больше любишь?
    /meat3 мясо  
    /grass3  растительная пища 
    '''
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['meat1' ])#лесное хищное животное
def meat(message: telebot.types.Message):
    text='''Отлично, ты больше любишь мясо!
    А вот и следующий вопрос:
    Какого ты размера?
    /big1   большой 
    /medium1   средний
    /small1  маленький'''
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['meat2'])# хищное животное из джунглей
def meat(message: telebot.types.Message):
    text = '''Отлично, ты больше любишь мясо!
        А вот и следующий вопрос:
        Какого ты размера?
        /big2  или напиши большой 
        /medium2  или напиши средний
        /small2 или напиши маленький'''
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['meat3' ])#хищное жтвотное из саванны
def meat(message: telebot.types.Message):
    text = '''Отлично, ты больше любишь мясо!
    А вот и следующий вопрос:
    Какого ты размера?
    /big3  или напиши большой
    /mrdium3  или напиши средний
    /small3  или напиши маленький'''
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['grass1'])#травоядные из леса
def grass(message: telebot.types.Message):
    text='''Отлично, ты больше любишь растительную пищу!
    А вот и следующий вопрос:
    Какого ты размера?
    /big4 или напиши большой
    /medium4  или напиши средний 
    /small4  или напиши маленький'''
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['grass2'])#травоядные из джунглей
def grass(message: telebot.types.Message):
    text = '''Отлично, ты больше любишь растительную пищу!
     А вот и следующий вопрос:
    Какого ты размера?
    /big5 или напиши большой
    /medium5️  или напиши средний 
    /small5  или напиши маленький'''
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['grass3'])#травоядные из саванны
def grass(message: telebot.types.Message):
    text = '''Отлично, ты больше любишь растительную пищу!
     А вот и следующий вопрос:
    Какого ты размера?
    /big6  большой
    /medium6  средний
    /small6 маленький'''
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands= ['big1'])#1 мясо
def big(message: telebot.types.Message):
    text = '''Мне кажется я знаю кто является твоим тотемным животным. Интересно?
    Чтобы узнать нажми: /myanimalbr'''
    bot.send_message(message.chat.id,text)
@bot.message_handler(commands= ['big2'])#2 трава
def big(message: telebot.types.Message):
    text = '''Мне кажется я знаю кто является твоим тотемным животным. Интересно?
    Чтобы узнать нажми: /myanimalml'''
    bot.send_message(message.chat.id,text)
@bot.message_handler(commands= ['big3'])#3 мясо
def big(message: telebot.types.Message):
    text = '''Мне кажется я знаю кто является твоим тотемным животным. Интересно?
    Чтобы узнать нажми: /myanimalgr'''
    bot.send_message(message.chat.id,text)
@bot.message_handler(commands= ['big4️'])#4 трава
def big(message: telebot.types.Message):
    text = '''Мне кажется я знаю кто является твоим тотемным животным. Интересно?
    Чтобы узнать нажми: /myanimaltr'''
    bot.send_message(message.chat.id,text)
@bot.message_handler(commands= ['big5'])#5 мясо
def big(message: telebot.types.Message):
    text = '''Мне кажется я знаю кто является твоим тотемным животным. Интересно?
    Чтобы узнать нажми: /myanimallv'''
    bot.send_message(message.chat.id,text)
@bot.message_handler(commands= ['big6'])#6 трава
def big(message: telebot.types.Message):
    text = '''Мне кажется я знаю кто является твоим тотемным животным. Интересно?
    Чтобы узнать нажми: /myanimalcn'''
    bot.send_message(message.chat.id,text)

@bot.message_handler(commands=['medium1'])#1 мясо
def medium(message: telebot.types.Message):
    text = '''Мне кажется я знаю кто является твоим тотемным животным. Интересно?
    Чтобы узнать нажми: /myanimalwl'''
    bot.send_message(message.chat.id, text)
@bot.message_handler(commands=['medium2'])#2 трава
def medium(message: telebot.types.Message):
    text = '''Мне кажется я знаю кто является твоим тотемным животным. Интересно?
    Чтобы узнать нажми: /myanimaldr'''
    bot.send_message(message.chat.id, text)
@bot.message_handler(commands=['medium3'])#3 мясо
def medium(message: telebot.types.Message):
    text = '''Мне кажется я знаю кто является твоим тотемным животным. Интересно?
    Чтобы узнать нажми: /myanimalot'''
    bot.send_message(message.chat.id, text)
@bot.message_handler(commands=['medium4'])#4 трава
def medium(message: telebot.types.Message):
    text = '''Мне кажется я знаю кто является твоим тотемным животным. Интересно?
    Чтобы узнать нажми: /myanimalkr'''
    bot.send_message(message.chat.id, text)
@bot.message_handler(commands=['medium5'])#5 мясо
def medium(message: telebot.types.Message):
    text = '''Мне кажется я знаю кто является твоим тотемным животным. Интересно?
    Чтобы узнать нажми: /myanimalgd'''
    bot.send_message(message.chat.id, text)
@bot.message_handler(commands=['medium6'])#6 трава
def medium(message: telebot.types.Message):
    text = '''Мне кажется я знаю кто является твоим тотемным животным. Интересно?
    Чтобы узнать нажми: /myanimalgl'''
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['small1'])#1 мясо
def small(message: telebot.types.Message):
    text = '''Мне кажется я знаю кто является твоим тотемным животным. Интересно?
    Чтобы узнать нажми: /myanimalnl'''
    bot.send_message(message.chat.id, text)
@bot.message_handler(commands=['small2'])#2 трава
def small(message: telebot.types.Message):
    text = '''Мне кажется я знаю кто является твоим тотемным животным. Интересно?
    Чтобы узнать нажми: /myanimalbl'''
    bot.send_message(message.chat.id, text)
@bot.message_handler(commands=['small3'])#3 мясо
def small(message: telebot.types.Message):
    text = '''Мне кажется я знаю кто является твоим тотемным животным. Интересно?
    Чтобы узнать нажми: /myanimalyi'''
    bot.send_message(message.chat.id, text)
@bot.message_handler(commands=['small4'])#4 трава
def small(message: telebot.types.Message):
    text = '''Мне кажется я знаю кто является твоим тотемным животным. Интересно?
    Чтобы узнать нажми: /myanimalom'''
    bot.send_message(message.chat.id, text)
@bot.message_handler(commands=['small5'])#5 мясо
def small(message: telebot.types.Message):
    text = '''Мне кажется я знаю кто является твоим тотемным животным. Интересно?
    Чтобы узнать нажми: /myanimalkk'''
    bot.send_message(message.chat.id, text)
@bot.message_handler(commands=['small6'])#6 трава
def small(message: telebot.types.Message):
    text = '''Мне кажется я знаю кто является твоим тотемным животным. Интересно?
    Чтобы узнать нажми: /myanimaldz'''
    bot.send_message(message.chat.id, text)



@bot.message_handler(commands=['myanimalbr'])#1
def result(message: telebot.types.Message):
        bot.send_message(message.chat.id, '''Да ты же медведь!
Хочешь начать еще раз?/start
Если вы хотите взять опеку над этим животным, свяжитесь с сотрудником зопарка: 
    Semensokolov2206@icloud.com''')

@bot.message_handler(commands=['myanimalml'])#2
def result(message: telebot.types.Message):
        bot.send_message(message.chat.id, '''Да ты же лось!
Хочешь начать еще раз?/start
Если вы хотите взять опеку над этим животным, свяжитесь с сотрудником зопарка: 
    Semensokolov2206@icloud.com''')

@bot.message_handler(commands=['myanimalwl'])#3
def result(message: telebot.types.Message):
        bot.send_message(message.chat.id, '''Да ты же волк!
Хочешь начать еще раз?/start
Если вы хотите взять опеку над этим животным, свяжитесь с сотрудником зопарка: 
    Semensokolov2206@icloud.com''')

@bot.message_handler(commands=['myanimaldr'])#4
def result(message: telebot.types.Message):
        bot.send_message(message.chat.id, '''Да ты же олень!
Хочешь начать еще раз?/start
Если вы хотите взять опеку над этим животным, свяжитесь с сотрудником зопарка: 
    Semensokolov2206@icloud.com''')

@bot.message_handler(commands=['myanimalnl'])#5
def result(message: telebot.types.Message):
        bot.send_message(message.chat.id, '''Да ты же манул! 
Хочешь начать еще раз?/start
Если вы хотите взять опеку над этим животным, свяжитесь с сотрудником зопарка: 
    Semensokolov2206@icloud.com''')

@bot.message_handler(commands=['myanimalbl'])#6
def result(message: telebot.types.Message):
        bot.send_message(message.chat.id, '''Да ты же белка!
Хочешь начать еще раз?/start
Если вы хотите взять опеку над этим животным, свяжитесь с сотрудником зопарка: 
    Semensokolov2206@icloud.com''')

@bot.message_handler(commands=['myanimalgr'])#7
def result(message: telebot.types.Message):
        bot.send_message(message.chat.id, '''Да ты же тигр!
Хочешь начать еще раз?/start
Если вы хотите взять опеку над этим животным, свяжитесь с сотрудником зопарка: 
    Semensokolov2206@icloud.com''')

@bot.message_handler(commands=['myanimaltr'])#8
def result(message: telebot.types.Message):
        bot.send_message(message.chat.id, '''Да ты же тапир!
Хочешь начать еще раз?/start
Если вы хотите взять опеку над этим животным, свяжитесь с сотрудником зопарка: 
    Semensokolov2206@icloud.com''')

@bot.message_handler(commands=['myanimalot'])#9
def result(message: telebot.types.Message):
        bot.send_message(message.chat.id, '''Да ты же оцелот!
Хочешь начать еще раз?/start
Если вы хотите взять опеку над этим животным, свяжитесь с сотрудником зопарка: 
    Semensokolov2206@icloud.com''')

@bot.message_handler(commands=['myanimalkr'])#10
def result(message: telebot.types.Message):
        bot.send_message(message.chat.id, '''Да ты же капибара!
Хочешь начать еще раз?/start
Если вы хотите взять опеку над этим животным, свяжитесь с сотрудником зопарка: 
    Semensokolov2206@icloud.com''')

@bot.message_handler(commands=['myanimalyi'])#11
def result(message: telebot.types.Message):
        bot.send_message(message.chat.id, '''Да ты же ягуардини!
Хочешь начать еще раз?/start
Если вы хотите взять опеку над этим животным, свяжитесь с сотрудником зопарка: 
    Semensokolov2206@icloud.com''')

@bot.message_handler(commands=['myanimalom'])#12
def result(message: telebot.types.Message):
        bot.send_message(message.chat.id, '''Да ты же опоссум!
Хочешь начать еще раз?/start
Если вы хотите взять опеку над этим животным, свяжитесь с сотрудником зопарка: 
    Semensokolov2206@icloud.com''')

@bot.message_handler(commands=['myanimallv'])#13
def result(message: telebot.types.Message):
        bot.send_message(message.chat.id, '''Да ты же лев!
Хочешь начать еще раз?/start
Если вы хотите взять опеку над этим животным, свяжитесь с сотрудником зопарка: 
    Semensokolov2206@icloud.com''')

@bot.message_handler(commands=['myanimalcn'])#14
def result(message: telebot.types.Message):
        bot.send_message(message.chat.id, '''Да ты же слон!
Хочешь начать еще раз?/start        
Если вы хотите взять опеку над этим животным, свяжитесь с сотрудником зопарка: 
    Semensokolov2206@icloud.com''')

@bot.message_handler(commands=['myanimalgd'])#15
def result(message: telebot.types.Message):
        bot.send_message(message.chat.id, '''Да ты же гепард!
Хочешь начать еще раз?/start
Если вы хотите взять опеку над этим животным, свяжитесь с сотрудником зопарка: 
    Semensokolov2206@icloud.com''')

@bot.message_handler(commands=['myanimalgl'])#16
def result(message: telebot.types.Message):
        bot.send_message(message.chat.id, '''Да ты же газель! 
Хочешь начать еще раз?/start
Если вы хотите взять опеку над этим животным, свяжитесь с сотрудником зопарка: 
    Semensokolov2206@icloud.com''')

@bot.message_handler(commands=['myanimalkk'])#17
def result(message: telebot.types.Message):
        bot.send_message(message.chat.id, '''Да ты же каракл! 
Хочешь начать еще раз?/start
Если вы хотите взять опеку над этим животным, свяжитесь с сотрудником зопарка: 
    Semensokolov2206@icloud.com''')

@bot.message_handler(commands=['myanimaldz'])#18
def result(message: telebot.types.Message):
        bot.send_message(message.chat.id, f'''да ты же дикобраз! 
Хочешь начать еще раз?/start
Если вы хотите взять опеку над этим животным, свяжитесь с сотрудником зопарка: 
    Semensokolov2206@icloud.com''')



bot.polling(none_stop=True ,interval=0)
