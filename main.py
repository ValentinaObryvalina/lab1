'''registration():
    original_password = "admin"

    while True:
        password = input("введите пароль: ")
        if password == original_password:
            return "Пароль принят"
        else:
            print("Пароль не принят")'''

'''place_in_train():
    aside_places = [number for number in range(37, 55)]
    number_place = int(input("Введите номер места: "))
    if number_place in aside_places:
        if number_place // 2 == 0:
            print("боковое верхнее")
        else:
            print("боковое нижнее")
    else:
        if number_place // 2 == 0:
            print("верхнее в купе")
        else:
            print("нижнее в купе")'''

'''year = int(input())
if (year %4 == 0) and (year % 100 != 0) or (year % 400 ==0):
    print('високосный')
else:
    print('не високосный')'''

'''colors=('красный','синий', 'желтый')
c1=input()
c2=input()
if c1 in colors and c2 in colors:
    if c1 != c2:
        if (c1 in ('красный','желтый')) and (c2 in ('красный','желтый')):
            print ('оранжевый')
        if (c1 in ('красный','синий')) and (c2 in ('красный','синий')):
            print ('фиолетовый')
        if (c1 in ('желтый', 'синий')) and (c2 in ('желтый', 'синий')):
            print ('зеленый')
    else:
        print(c1)
else:
    print("ошибка")'''

