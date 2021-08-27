heightt = int(input('Введите рост призывника\n'))
age = int(input('Введите возраст призывника\n'))
child = int(input('Введите количество детей призывника\n'))
study = input('Учится ли он сейчас ?\n')



if age < 18 or age > 27 or child >= 3 or study == 'Да':
    print('Призывник не годен к военной службе')

elif  heightt <= 165:
    print('Призывник годен в танковые войска')



elif  heightt  <= 175:
    print('Призывник годен в мотострелковые  войска')









