def advice():
    age = int(input("Сколько вам лет? "))
    if age <= 0:
        return ("Вы в процессе") 
    elif 0 < age <= 6:
        return('Ходите с дет. сад')
    elif 7 <= age <= 17:
        return('Учитесь в школе')
    elif 18 <= age <= 23:
        return ('Учитесь в ВУЗе')
    else:
        return ('Вам пора работать')
advice()