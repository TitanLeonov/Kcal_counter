import telebot
import calc
import sqlite3
from spellchecker import SpellChecker

con = sqlite3.connect("food.db", check_same_thread=False)
cur = con.cursor()


bot = telebot.TeleBot('5510516119:AAFv8yr225_zo-Q9d8ao5QhBggFM7E9c44U')

global eaten_food
eaten_food = []

global parametrs
parametrs = []

spell = SpellChecker(language="ru")

# global gender, age, weight, height, kf, mode, bmr_mode, bmr
# gender = ''
# age = 0
# weight = 0
# height = 0
# kf = 1
# mode = 0
# brm = 0
# bmr_mode = 0
# kf = 1

# def Find_BMR(age,weight, height):
#     if (gender == 'м'):
#         bmr = 88.362 + (13.4 * weight) + (4.8 * height) - (5.677 * age)
#     elif (gender == 'ж'):
#         bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
#     else:
#         print('error has happend')
#     return bmr
# def Find_BMR_mode(bmr, mode):
#     if (mode == 1):
#         bmr_mode = bmr*0.85
#     elif (mode == 2):
#         bmr_mode = bmr
#     elif (mode == 3):
#         bmr_mode = bmr*1.2
#     return bmr_mode
# def Day_kcal(age, weight, height):
#     bmr = Find_BMR(age,weight, height)
#     bmr_mode = Find_BMR_mode(bmr)
#     message_text = ''
#     if (mode == 1):
#         message_text =''
#         message_text = message_text + f'советуем употреблять примерно {bmr_mode:.1f} ккал в день,\n'
#         # print(f'советуем употреблять примерно {bmr_mode:.1f} ккал в день,')
#         message_text = message_text + f'не менее {weight*0.75:.1f}-{weight} г белков в день, оптимально {weight*1.5}-{weight*2},\n'
#         # print(f'не менее {weight*0.75:.1f}-{weight} г белков в день, оптимально {weight*1.5}-{weight*2},')
#         if (weight*0.7 <= 30):
#             message_text = message_text + f'не менее 30 г жиров в день но не более {weight*2} г жиров в день\n'
#             # print(f'не менее 30 г жиров в день но не более {weight*2} г жиров в день')
#         else:
#             message_text = message_text + f'{weight} г жиров в день'
#             # print(f'{weight} г жиров в день')
#         message_text = message_text + f'и примерно {bmr_mode*0.4/4:.1f}-{bmr_mode*0.5/4:.1f} г углеводов, желательно не менее {bmr_mode*0.3/4:.1f}-{bmr_mode*0.4/4:.1f} из них сложных'
#         # print(f'и примерно {bmr_mode*0.4/4:.1f}-{bmr_mode*0.5/4:.1f} г углеводов, желательно не менее {bmr_mode*0.3/4:.1f}-{bmr_mode*0.4/4:.1f} из них сложных')
#
#
#     if (mode == 2):
#         message_text = message_text + f'советуем употреблять примерно {bmr_mode:.1f} ккал в день,\n'
#         # print(f'советуем употреблять примерно {bmr_mode:.1f} ккал в день,')
#         message_text = message_text + f'не менее {weight * 0.75:.1f}-{weight} г белков в день, оптимально {weight * 1.5}-{weight * 2},\n'
#         # print(f'не менее {weight*0.75:.1f}-{weight} г белков в день, оптимально {weight*1.5}-{weight*2},')
#         if (weight*0.7 <= 30):
#             message_text = message_text + f'не менее 30 г жиров в день но не более {weight*2} г жиров в день\n'
#             # print(f'не менее 30 г жиров в день но не более {weight*2} г жиров в день')
#         else:
#             message_text = message_text + f'{weight} г жиров в день'
#             # print(f'{weight} г жиров в день')
#         message_text = message_text + f'и примерно {bmr_mode*0.4/4:.1f}-{bmr_mode*0.5/4:.1f} г углеводов, желательно не менее {bmr_mode*0.3/4:.1f}-{bmr_mode*0.4/4:.1f} из них сложных'
#         # print(f'и примерно {bmr_mode*0.4/4:.1f}-{bmr_mode*0.5/4:.1f} г углеводов, желательно не менее {bmr_mode*0.3/4:.1f}-{bmr_mode*0.4/4:.1f} из них сложных')
#
#
#     if (mode == 3):
#         message_text = message_text + f'советуем употреблять примерно {bmr_mode:.1f} ккал в день,\n'
#         # print(f'советуем употреблять примерно {bmr_mode:.1f} ккал в день,')
#         # print(f'не менее {weight*1.5:.1f}-{weight*2} г белков в день, оптимально {weight*2.5}-{weight*3},')
#         message_text = message_text + f'не менее {weight * 0.75:.1f}-{weight} г белков в день, оптимально {weight * 1.5}-{weight * 2},\n'
#         if (weight*0.7 <= 30):
#             message_text = message_text + f'не менее 30 г жиров в день но не более {weight*2} г жиров в день\n'
#             # print(f'не менее 30 г жиров в день но не более {weight*2} г жиров в день')
#         else:
#             message_text = message_text + f'{weight} г жиров в день'
#             # print(f'{weight} г жиров в день')
#         message_text = message_text + f'и примерно {bmr_mode*0.4/4:.1f}-{bmr_mode*0.5/4:.1f} г углеводов, желательно не менее {bmr_mode*0.3/4:.1f}-{bmr_mode*0.4/4:.1f} из них сложных'
#         # print(f'и примерно {bmr_mode*0.4/4:.1f}-{bmr_mode*0.5/4:.1f} г углеводов, желательно не менее {bmr_mode*0.3/4:.1f}-{bmr_mode*0.4/4:.1f} из них сложных')
#     return message_text
def Search_name(a):
    s = []
    s.append(a)
    f = (a.split(' '))

    for x in f: s.append(x)
    for i in range(len(s)):
        if len(s[i]) >= 4 and (s[i][-1] == 'а' or s[i][-1] == 'и' or s[i][-1] == 'ы'):
            s[i] = s[i][:len(s[i]) - 1]

    for x in s:
        print(x)
        sql = f"SELECT * FROM food WHERE name LIKE '%{x}%'"
    cur.execute(sql)
    return (cur.fetchmany(10))

# 'Введите уровень активности:\n, Минимальный уровень активности — 1.2,\nНизкий уровень активности — 1.375,\nСредний уровень активности — 1.55,\nВысокий уровень — 1.725,\nОчень высокий —  1.9:\n')
@bot.message_handler(commands=["start", 'help'])
def start(m):
    bot.send_message(m.chat.id, 'Введите любой продукт или блюдо: ')
    bot.send_message(m.chat.id,
    'Введите "сколько сьел", чтобы узнать сколько вы сегодня сьели; "добавить свое", чтобы добавить свое блюдо или продукт, или "рассчитать норм ккал" чтобы рассчитать суточную номру КБЖУ в день')

@bot.message_handler(commands=['add_norm_kcal'])
def norm_kcal(message):
    print(parametrs)

    def input_gender(message):
        if (message.text.lower() == 'отменить'):
            pass
        else:
            try:
                global gender
                if (message.text == 'м' or message.text == 'ж'):
                    gender = message.text
                else:
                    print(gender)
                bot.send_message(message.chat.id, 'Введите свой возраст')
                bot.register_next_step_handler(message, input_age)
            except:
                bot.send_message(message.chat.id, 'Пожалуйста, ответье буквой "м" или "ж"')
                bot.register_next_step_handler(message, input_gender)

    def input_age(message):
        if (message.text.lower() == 'отменить'):
            pass
        else:
            try:
                global age
                if (0 >= int(message.text) or int(message.text) >= 100):
                    bot.send_message(message.chat.id, f'Вам не может быть {message.text} лет.')
                    print(age)
                age = float(message.text)
                bot.send_message(message.chat.id, 'Введите свой вес (кг)')
                bot.register_next_step_handler(message, input_weight)
            except:
                bot.send_message(message.chat.id, 'Пожалуйста введите возраст целым числом')
                bot.register_next_step_handler(message, input_age)

    def input_weight(message):
        if (message.text.lower() == 'отменить'):
            pass
        else:
            try:
                global weight
                weight = float(message.text)
                bot.send_message(message.chat.id, 'Введите свой рост (см)')
                bot.register_next_step_handler(message, input_height)
            except:
                bot.send_message(message.chat.id, 'Пожалуйста введите свой вес в кг цифрами')
                bot.register_next_step_handler(message, input_weight)

    def input_height(message):
        if (message.text.lower() == 'отменить'):
            pass
        else:
            try:
                global height
                height = float(message.text)
                bot.send_message(message.chat.id, 'Введите свой уровень активности:')
                bot.send_message(message.chat.id,
                                 'Минимальный уровень активности — 1,\nНизкий уровень активности — 2,\nСредний уровень активности — 3,\nВысокий уровень — 4,\nОчень высокий —  5:\n')
                bot.register_next_step_handler(message, input_kf)
            except:
                bot.send_message(message.chat.id, 'Пожалуйста, введите свой рост цифрами')
                bot.register_next_step_handler(message, input_height)

    def input_kf(message):
        if (message.text.lower() == 'отменить'):
            pass
        else:
            try:
                global kf
                if (int(message.text) == 1):
                    kf = 1.2
                if (int(message.text) == 2):
                    kf = 1.375
                if (int(message.text) == 3):
                    kf = 1.55
                if (int(message.text) == 4):
                    kf = 1.725
                if (int(message.text) == 5):
                    kf = 1.9
                bot.send_message(message.chat.id, 'Выберите и введите свою цель: ')
                bot.send_message(message.chat.id, 'Похудеть - 1, \nПоддерживать свой вес - 2, \nНабрать массу - 3')
                bot.register_next_step_handler(message, input_mode)
            except:
                bot.send_message(message.chat.id, 'Пожалуйста, ответье числом от 1 до 5')
                bot.register_next_step_handler(message, input_kf)

    def input_mode(message):
        if (message.text.lower() == 'отменить'):
            pass
        else:
            try:
                global mode
                if (1 <= int(message.text) <= 5):
                    mode = int(message.text)
                bmr_mode = calc.Find_BMR_mode(calc.Find_BMR(gender, age, weight, height), mode)
                bot.send_message(message.chat.id, f'{calc.Day_kcal(gender, age, weight, height, mode)}')
                d = {'Пол: ': gender, 'Возраст:': age, 'Вес: ': weight, 'Рост: ': height, 'КФ: ': kf, 'Мод: ': mode,
                     'bmr: ': calc.Find_BMR(gender, age, weight, height), 'bmr_mode: ': bmr_mode}
                if (parametrs != [0]):
                    parametrs.clear()
                parametrs.append(d)


            except:
                bot.send_message(message.chat.id, 'Пожалуйста, ответье числом от 1 до 3')
                bot.register_next_step_handler(message, input_mode)

    global bmr_mode
    bot.send_message(message.chat.id, 'Введите свой пол (м/ж)')
    bot.register_next_step_handler(message, input_gender)

@bot.message_handler(commands=['add_my'])
def add_my(message):
    bot.send_message(message.chat.id, 'введите название')

    def input_name(message):
        if (message.text.lower() == 'отменить'):
            pass
        else:
            global name_self
            name_self = message.text
            print(name_self)
            bot.send_message(message.chat.id, 'введите калойрийность(ккал)')
            bot.register_next_step_handler(message, input_ccal)

    def input_ccal(message):
        if (message.text.lower() == 'отменить'):
            pass
        else:
            try:
                global ccal_self
                ccal_self = float(message.text)
                print(ccal_self)
                bot.send_message(message.chat.id, 'введите Белки на 100г (г)')
                bot.register_next_step_handler(message, input_prot)
            except:
                bot.send_message(message.chat.id, 'Пожалуйста введите калорийность цифрами и без пробелов')
                bot.register_next_step_handler(message, input_ccal)

    def input_prot(message):
        if (message.text.lower() == 'отменить'):
            pass
        else:
            try:
                global prot_self
                prot_self = float(message.text)
                print(prot_self)
                bot.send_message(message.chat.id, 'введите Жиры на 100г (г)')
                bot.register_next_step_handler(message, input_fats)
            except:
                bot.send_message(message.chat.id,
                                 'Пожалуйста введите Белки(г) цифрами и без пробелов или напишите "Отменить"')
                bot.register_next_step_handler(message, input_prot)

    def input_fats(message):
        if (message.text.lower() == 'отменить'):
            pass
        else:
            try:
                global fats_self
                fats_self = float(message.text)
                print(fats_self)
                bot.send_message(message.chat.id, 'введите Углеводы на 100г (г)')
                bot.register_next_step_handler(message, input_cbh)
            except:
                bot.send_message(message.chat.id,
                                 'Пожалуйста введите Жиры (г) цифрами и без пробелов или напишите "Отменить"')
                bot.register_next_step_handler(message, input_fats)

    def input_cbh(message):
        if (message.text.lower() == 'отменить'):
            pass
        else:
            try:
                global cbh_self
                cbh_self = float(message.text)
                print(cbh_self)
                bot.send_message(message.chat.id, 'введите вес (г)')
                bot.register_next_step_handler(message, input_weight)
            except:
                bot.send_message(message.chat.id,
                                 'Пожалуйста введите Углеводы (г) цифрами и без пробелов или напишите "Отменить"')
                bot.register_next_step_handler(message, input_cbh)

    def input_weight(message):
        if (message.text.lower() == 'отменить'):
            pass
        else:
            try:
                weight_self = float(message.text)
                print(weight_self)
                d = {"Название": name_self, 'ккал': ccal_self * weight_self / 100.0,
                     'Белки (г)': prot_self * weight_self / 100.0,
                     'Жиры (г)': fats_self * weight_self / 100.0,
                     'Углеводы (г)': cbh_self * weight_self / 100.0,
                     'вес (г)': weight_self}
                eaten_food.append(d)
                bot.send_message(message.chat.id, 'Записал :)')
                print(eaten_food)
            except:
                bot.send_message(message.chat.id,
                                 'Пожалуйста введите Вес (г) цифрами и без пробелов или напишите "Отменить"')
                bot.register_next_step_handler(message, input_weight)

    bot.register_next_step_handler(message, input_name)
@bot.message_handler(content_types=['text'])
def handle_text(message):


    if (message.text.lower() == 'рассчитать норм ккал'):
        print(parametrs)
        def input_gender(message):
            if (message.text.lower() == 'отменить'):
                pass
            else:
                try:
                    global gender
                    if (message.text == 'м' or message.text == 'ж'):
                        gender = message.text
                    else:
                        print(gender)
                    bot.send_message(message.chat.id, 'Введите свой возраст')
                    bot.register_next_step_handler(message, input_age)
                except:
                    bot.send_message(message.chat.id, 'Пожалуйста, ответье буквой "м" или "ж"')
                    bot.register_next_step_handler(message, input_gender)

        def input_age(message):
            if (message.text.lower() == 'отменить'):
                pass
            else:
                try:
                    global age
                    if ( 0 >= int(message.text) or int(message.text) >=100):
                        bot.send_message(message.chat.id, f'Вам не может быть {message.text} лет.')
                        print(age)
                    age = float(message.text)
                    bot.send_message(message.chat.id, 'Введите свой вес (кг)')
                    bot.register_next_step_handler(message, input_weight)
                except:
                    bot.send_message(message.chat.id, 'Пожалуйста введите возраст целым числом')
                    bot.register_next_step_handler(message, input_age)

        def input_weight(message):
            if (message.text.lower() == 'отменить'):
                pass
            else:
                try:
                    global weight
                    weight = float(message.text)
                    bot.send_message(message.chat.id, 'Введите свой рост (см)')
                    bot.register_next_step_handler(message, input_height)
                except:
                    bot.send_message(message.chat.id, 'Пожалуйста введите свой вес в кг цифрами')
                    bot.register_next_step_handler(message, input_weight)

        def input_height(message):
            if (message.text.lower() == 'отменить'):
                pass
            else:
                try:
                    global height
                    height = float(message.text)
                    bot.send_message(message.chat.id, 'Введите свой уровень активности:')
                    bot.send_message(message.chat.id,'Минимальный уровень активности — 1,\nНизкий уровень активности — 2,\nСредний уровень активности — 3,\nВысокий уровень — 4,\nОчень высокий —  5:\n')
                    bot.register_next_step_handler(message, input_kf)
                except:
                    bot.send_message(message.chat.id, 'Пожалуйста, введите свой рост цифрами')
                    bot.register_next_step_handler(message, input_height)

        def input_kf(message):
            if (message.text.lower() == 'отменить'):
                pass
            else:
                try:
                    global kf
                    if (int(message.text) == 1):
                        kf = 1.2
                    if (int(message.text) == 2):
                        kf = 1.375
                    if (int(message.text) == 3):
                        kf = 1.55
                    if (int(message.text) == 4):
                        kf = 1.725
                    if (int(message.text) == 5):
                        kf = 1.9
                    bot.send_message(message.chat.id, 'Выберите и введите свою цель: ')
                    bot.send_message(message.chat.id, 'Похудеть - 1, \nПоддерживать свой вес - 2, \nНабрать массу - 3')
                    bot.register_next_step_handler(message, input_mode)
                except:
                    bot.send_message(message.chat.id, 'Пожалуйста, ответье числом от 1 до 5')
                    bot.register_next_step_handler(message, input_kf)

        def input_mode(message):
            if (message.text.lower() == 'отменить'):
                pass
            else:
                try:
                    global mode
                    if ( 1 <=int(message.text) <=5):
                        mode = int(message.text)
                    bmr_mode = calc.Find_BMR_mode(calc.Find_BMR(gender, age, weight, height), mode)
                    bot.send_message(message.chat.id, f'{calc.Day_kcal(gender, age, weight, height, mode)}')
                    d = {'Пол: ': gender, 'Возраст:': age, 'Вес: ': weight, 'Рост: ': height, 'КФ: ': kf, 'Мод: ': mode,
                         'bmr: ': calc.Find_BMR(gender, age, weight, height), 'bmr_mode: ': bmr_mode}
                    if (parametrs != [0]):
                        parametrs.clear()
                    parametrs.append(d)


                except:
                    bot.send_message(message.chat.id, 'Пожалуйста, ответье числом от 1 до 3')
                    bot.register_next_step_handler(message, input_mode)

        global bmr_mode
        bot.send_message(message.chat.id, 'Введите свой пол (м/ж)')
        bot.register_next_step_handler(message, input_gender)

    elif (message.text.lower() == 'добавить своё' or message.text.lower() == 'добавить свое'):
        bot.send_message(message.chat.id, 'введите название')

        def input_name(message):
            if (message.text.lower() == 'отменить'):
                pass
            else:
                global name_self
                name_self = message.text
                print(name_self)
                bot.send_message(message.chat.id, 'введите калойрийность(ккал)')
                bot.register_next_step_handler(message, input_ccal)


        def input_ccal(message):
            if (message.text.lower() == 'отменить'):
                pass
            else:
                try:
                    global ccal_self
                    ccal_self = float(message.text)
                    print(ccal_self)
                    bot.send_message(message.chat.id, 'введите Белки на 100г (г)')
                    bot.register_next_step_handler(message, input_prot)
                except:
                    bot.send_message(message.chat.id, 'Пожалуйста введите калорийность цифрами и без пробелов')
                    bot.register_next_step_handler(message, input_ccal)


        def input_prot(message):
            if (message.text.lower() == 'отменить'):
                pass
            else:
                try:
                    global prot_self
                    prot_self = float(message.text)
                    print(prot_self)
                    bot.send_message(message.chat.id, 'введите Жиры на 100г (г)')
                    bot.register_next_step_handler(message, input_fats)
                except:
                    bot.send_message(message.chat.id, 'Пожалуйста введите Белки(г) цифрами и без пробелов или напишите "Отменить"')
                    bot.register_next_step_handler(message, input_prot)

        def input_fats(message):
            if (message.text.lower() == 'отменить'):
                pass
            else:
                try:
                    global fats_self
                    fats_self = float(message.text)
                    print(fats_self)
                    bot.send_message(message.chat.id, 'введите Углеводы на 100г (г)')
                    bot.register_next_step_handler(message, input_cbh)
                except:
                    bot.send_message(message.chat.id, 'Пожалуйста введите Жиры (г) цифрами и без пробелов или напишите "Отменить"')
                    bot.register_next_step_handler(message, input_fats)

        def input_cbh(message):
            if (message.text.lower() == 'отменить'):
                pass
            else:
                try:
                    global cbh_self
                    cbh_self = float(message.text)
                    print(cbh_self)
                    bot.send_message(message.chat.id, 'введите вес (г)')
                    bot.register_next_step_handler(message, input_weight)
                except:
                    bot.send_message(message.chat.id, 'Пожалуйста введите Углеводы (г) цифрами и без пробелов или напишите "Отменить"')
                    bot.register_next_step_handler(message, input_cbh)

        def input_weight(message):
            if (message.text.lower() == 'отменить'):
                pass
            else:
                try:
                    weight_self = float(message.text)
                    print(weight_self)
                    d = {"Название": name_self, 'ккал': ccal_self * weight_self / 100.0,
                         'Белки (г)': prot_self * weight_self / 100.0,
                         'Жиры (г)': fats_self * weight_self / 100.0,
                         'Углеводы (г)': cbh_self * weight_self / 100.0,
                         'вес (г)': weight_self}
                    eaten_food.append(d)
                    bot.send_message(message.chat.id, 'Записал :)')
                    print(eaten_food)
                except:
                    bot.send_message(message.chat.id, 'Пожалуйста введите Вес (г) цифрами и без пробелов или напишите "Отменить"')
                    bot.register_next_step_handler(message, input_weight)

        bot.register_next_step_handler(message, input_name)


    elif (message.text.lower() == 'сколько сьел' or message.text.lower() == 'сколько съел'):
        bot.send_message(message.chat.id, 'ща скажу')
        ccal = 0
        prot = 0
        fat = 0
        cb = 0
        for food in eaten_food:
            d = dict.copy(food)
            ccal += d['ккал']
            prot += d['Белки (г)']
            fat += d['Жиры (г)']
            cb += d['Углеводы (г)']
            bot.send_message(message.chat.id,
                             f'Название: {d["Название"]}\n ккал: {d["ккал"]}\nБелки (г): {d["Белки (г)"]}\n Жиры (г): {d["Жиры (г)"]}\n Углеводы (г): {d["Углеводы (г)"]}\nВес (г): {d["вес (г)"]}')
        bot.send_message(message.chat.id,
                         f'итого: ккал: {ccal}\nБелки (г): {prot}\nЖиры (г): {fat}\n Углеводы (г): {cb}')


    else:
        print(message.chat.id)
        s = message.text
    layout = dict(zip(map(ord, "qwertyuiop[]asdfghjkl;'zxcvbnm,./`"
                           'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'),
                           "йцукенгшщзхъфывапролджэячсмитьбю.ё"
                           'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'))
    word1=f"{s}".translate(layout)
    k=[]
    
    

    misspelled = spell.unknown([f"{word1}"])

    for word in misspelled:
        a = spell.correction(word)
        k.append(a)
        
    if len(k) == 0:
        axc = Search_name(str(word1).lower())
    
    else:
        w = k[0]
        axc = Search_name(str(w).lower())
    print(axc)
        i = 1
        for example in axc:
            bot.send_message(message.chat.id, f'Название: {example[0]}\nккал: {example[1]}\n Белки: {example[2]}\nЖиры: {example[3]}\nУглеводы: {example[4]}\n НОМЕР: {i}')
            i+=1

        def check(message):
            if (message.text.lower() == 'да'):
                bot.send_message(message.chat.id, "введите номер нрав еды, которую записать")
                bot.register_next_step_handler(message, check_number)
            elif (message.text.lower() == 'нет'):
                bot.send_message(message.chat.id, "попробуйте другой запрос или добавьте свое блюдо")
            else:
                bot.send_message(message.chat.id, "Пожалуйста, отметье да или нет")
                bot.register_next_step_handler(message, check)

        def check_number(message):
            if (message.text.lower() == 'отменить'):
                pass
            else:
                try:
                    global num
                    if (int(message.text) >= 1 and int(message.text) <= i - 1):
                        num = int(message.text)
                    else:
                        bot.send_message(message.chat.id, f"{num}")
                    print(num)
                    bot.send_message(message.chat.id, "Введите коллвичество еды (в граммах)")
                    bot.register_next_step_handler(message, check_weight)
                except:
                    bot.send_message(message.chat.id,
                                     f'Введите номер еды цифрой от 1 до {i - 1} или напишите "Отменить"')
                    bot.register_next_step_handler(message, check_number)

        def check_weight(message):
            if (message.text.lower() == 'отменить'):
                pass
            else:
                try:
                    global weight
                    weight = float(message.text)
                    print(weight)

                    bot.send_message(message.chat.id,
                                     f'{axc[int(num) - 1][0]}, {axc[int(num) - 1][1]}, вес: {weight} г')
                    d = {"Название": axc[int(num) - 1][0], 'ккал': float(axc[int(num) - 1][1]) * weight / 100.0,
                         'Белки (г)': float(axc[num - 1][2]) * weight / 100.0,
                         'Жиры (г)': float(axc[num - 1][3]) * weight / 100.0,
                         'Углеводы (г)': float(axc[num - 1][4]) * weight / 100.0,
                         'вес (г)': weight}
                    eaten_food.append(d)
                    bot.send_message(message.chat.id, 'Записал :)')
                    print(eaten_food)
                except:
                    bot.send_message(message.chat.id,
                                     'Пожалуйста введите Вес (г) цифрами и без пробелов или напишите "Отменить"')
                    bot.register_next_step_handler(message, check_weight)

        if (i != 1):
            bot.send_message(message.chat.id, 'хотите что-то добавить в список сьеденноего? (да/нет)')
            bot.register_next_step_handler(message, check)
        else:
            bot.send_message(message.chat.id, "Увы, по вашему запросу не было найдено ни одного блюда.")





bot.polling(none_stop=True, interval=0)
