# Проект FitLife - MVP версия 1.0
# описание проекта.
# Компания разрабатывает приложение,
# которое помогает людям следить за здоровьем.
# Мобильной версии пока нет,
# но инвесторы хотят увидеть работающий прототип уже завтра.

import sys

sys.stdout.reconfigure(encoding='utf-8')


print('Приветствую тебя! Фитнес - это новая жизнь !')
print('Как я могу к тебе обращаться ?')
user_name = input()

print('Какой у тебя возраст ?')
user_age = int(input())

print('Введи данные для предоставления рекомендаций')
print('Какой у тебя вес в кг (пример:1.23) ?')
user_weight = float(input())

print('Какой у тебя рост в метрах (пример:1.23) ?')
user_height = float(input())

# рассчитывает ИМТ, и выдает рекомендации.
bmi = user_weight / (user_height ** 2)

# расчет воды

WATER_PER_KG = 30
ML_IN_LITERS = 1000


water_ml = user_weight * WATER_PER_KG   # мл
water_needed = water_ml / ML_IN_LITERS  # получаем литры

# Отчет по метрикам пользователя
print('Я изучил твои данные и вот что: ')
print(f'Тебя зовут {user_name}, тебе {user_age}.')
print(f'Твой ИМТ - {round(bmi, 1)}')
print(f'Рекомендую пить воды: {round(water_needed, 1)} л. в сутки.')
print('Фитнес - это новая жизнь !')
print("Расчет окончен. Будьте здоровы!")
