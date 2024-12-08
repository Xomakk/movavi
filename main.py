import datetime
import sqlite3
import random
import telebot
current_datetime = datetime.datetime.now()
sp =""
sp +=str(current_datetime.day)+ " " +str(current_datetime.month)+ " "+str(current_datetime.year)
connection = sqlite3.connect("jelania.db")

cursor_object = connection.execute(
  """
    CREATE TABLE IF NOT EXISTS jelanis(
        order_id INTEGER PRIMARY KEY,
        chat_id INTEGER,
        jelania TEXT,
        data TEXT
    )
  """
)
a = """В этом году ты точно будешь с друзьями на одной волне! А ещё - в одной WiFi-сети, когда вы вместе придете на занятия в школу Movavi. 
Активируем IT-интуицию: в наступающем году ты сможешь создать самый крутой проект на своем курсе! 
Подходящий год для великих дел! Даже самые сложные задачки не устоят перед твоим энтузиазмом ☀️
У тебя появится особый "хакерский" навык — умение узнавать, кто съел последнее печенье, по одному взгляду на одногруппников. 
Предсказываем тебе урожай новых умений, крутых проектов — и много-много-много самых любимых печенек 🍪
Будет много крутых каток с друзьями! Но не забывай иногда выпускать телефон из рук. Говорят, катать на лыжах тоже интересно. 
В этом году на занятиях в школе Movavi у тебя появится крутой друг, который будет понимать все-все-все твои шутки!
Наши "да" в людях - быть похожим на тебя! Потому что ты очень-очень крутой :) Пусть этот год принесет тебе много радости! 
Босс айти - это про тебя. Да-да, не скромничай :) Желаем добиться еще больших высот в IT-мире, а мы тебе в этом поможем.
Твои успехи в новом году заметят все друзья - и захотят заниматься с тобой в одной группе 🤩
Звезды предсказывают, что в новом году ты справишься со всеми багами!
Твой уровень креативности взлетит до небес! Жди лавину гениальных идей для собственных проектов, которые удивят всех преподавателей.
В грядущем году ты освоишь новый IT-навык так же легко, как распаковываешь новогодние подарки!
Счастливого Нового Года! Пусть в этом году тебя ждут мега-каникулы с любимыми друзьями. Не забывайте делать перерывы от экранов - на улице отличная погода! 
В новом году ты обретешь суперсилу: превращать скучные задачи в увлекательные челленджи! 
Прогнозируем: твои проекты взорвут интернет! Жди миллионы лайков и репостов. 
В этом году твои проекты будут настолько крутыми, что даже самые требовательные преподаватели Movavi будут ставить тебе самые высокие оценки!
Ты научишься так быстро набирать код, что клавиатура будет звучать как музыка для ушей твоих одногруппников.
В этом году ты станешь настоящим гуру в области кибербезопасности и будешь помогать друзьям защищать свои устройства от хакеров.
Твои знания будут расти так быстро, что уже совсем скоро ты сможешь начать свой собственный стартап!"""
TOKEN = "7345251836:AAFyEw6TwmMl5YS0yWBtnYzenB4zu3llT3I"
bot = telebot.TeleBot(TOKEN)
connection.close()

@bot.message_handler(commands=['start'])
def handle_start(message):
    global a
    connection = sqlite3.connect("jelania.db")
    cursor_object = connection.execute(
        f"""
            SELECT jelania
            FROM jelanis
            WHERE chat_id = {message.chat.id}
        """
    )
    # достаем все данные и перебираем список
    current_datetime = datetime.datetime.now()
    sp =""
    sp +=str(current_datetime.day)+ " " +str(current_datetime.month)+ " "+str(current_datetime.year)
    g =cursor_object.fetchall()
    connection.close()
    if g==[]:
        g= a.split()
        connection = sqlite3.connect("jelania.db")
        cursor_object = connection.execute(f"""
        INSERT INTO jelanis(chat_id, jelania, data) 
        VALUES ({message.chat.id}, '{a}', '{sp}')
        """)
        connection.commit()
        connection.close()
    else:
        g = g[0][0].split("\n")
    connection = sqlite3.connect("jelania.db")
    cursor_object = connection.execute(
        f"""
            SELECT data
            FROM jelanis
            WHERE chat_id = {message.chat.id}
        """
    )
    sd = cursor_object.fetchall()[0][0]
    if sp!=sd:
        f = g[random.randint(0,len(g)-1)]
        g.remove(f)
        s =""
        for i in g:
            s+=i+"\n"

        if len(s)==0:
            s = a
        SQL_UPDATE_TABLE = f"""
        UPDATE jelanis
        SET jelania = '{s}', data = '{sp}'
        WHERE chat_id = {message.chat.id}
        """
        connection.execute(SQL_UPDATE_TABLE)
        connection.commit()
        bot.send_message(message.chat.id, f)
        connection.close()

bot.polling(non_stop=True, interval=1)