number_of_day = int(input('Введите день рождения от 1 до 31\n'))

number_of_mounth = int(input('Введите месяц рождения от 1 до 12\n'))

number_of_year = int(input('Введите год вашего рождения в формате - 19XX или 20XX\n'))

if (number_of_day >= 21 and number_of_day <= 31 and number_of_mounth == 3) or (
(number_of_day >= 1 and number_of_day <= 20 and number_of_mounth == 4)):
    print('Ваш знак зодиака - Овен ')
    break

elif (number_of_day >= 21 and number_of_day <= 31 and number_of_mounth == 4) or (
(number_of_day >= 1 and number_of_day <= 21 and number_of_mounth == 5)):
    print('Ваш знак зодиака - Телец ')
    break

elif (number_of_day >= 22 and number_of_day <= 31 and number_of_mounth == 5) or (
(number_of_day >= 1 and number_of_day <= 21 and number_of_mounth == 6)):
    print('Ваш знак зодиака - Близнецы ')
    break

elif (number_of_day >= 22 and number_of_day <= 31 and number_of_mounth == 6) or (
(number_of_day >= 1 and number_of_day <= 22 and number_of_mounth == 7)):
    print('Ваш знак зодиака - Рак ')
    break


elif (number_of_day >= 23 and number_of_day <= 31 and number_of_mounth == 7) or (
        number_of_day >= 1 and number_of_day <= 22 and number_of_mounth == 8):
    print('Ващ знак зодиака - Лев')

elif (number_of_day >= 24 and number_of_day <= 31 and number_of_mounth == 8) or (
        number_of_day >= 1 and number_of_day <= 23 and number_of_mounth == 9):
    print('Ващ знак зодиака - Дева')

elif (number_of_day >= 24 and number_of_day <= 31 and number_of_mounth == 9) or (
        number_of_day >= 1 and number_of_day <= 23 and number_of_mounth == 10):
    print('Ващ знак зодиака - Весы')

elif (number_of_day >= 24 and number_of_day <= 31 and number_of_mounth == 10) or (
        number_of_day >= 1 and number_of_day <= 22 and number_of_mounth == 11):
    print('Ващ знак зодиака - Скорпион')

elif (number_of_day >= 24 and number_of_day <= 31 and number_of_mounth == 11) or (
        number_of_day >= 1 and number_of_day <= 21 and number_of_mounth == 12):
    print('Ващ знак зодиака - Стрелец')

elif (number_of_day >= 22 and number_of_day <= 31 and number_of_mounth == 12) or (
        number_of_day >= 1 and number_of_day <= 20 and number_of_mounth == 1):
    print('Ващ знак зодиака - Козерог')

elif (number_of_day >= 21 and number_of_day <= 31 and number_of_mounth == 1) or (
        number_of_day >= 1 and number_of_day <= 18 and number_of_mounth == 2):
    print('Ващ знак зодиака - Водолей')

elif (number_of_day >= 19 and number_of_day <= 31 and number_of_mounth == 2) or (
        number_of_day >= 1 and number_of_day <= 20 and number_of_mounth == 2):
    print('Ващ знак зодиака - Рыбы')