# Задание №1 (оператор IF)
def advice(age):
    if age <= 0:
        return ("Вы в процессе") 
    elif age <= 6:
        return('Ходите с дет. сад')
    elif 7 <= age <= 17:
        return('Учитесь в школе')
    elif 18 <= age <= 23:
        return ('Учитесь в ВУЗе')
    else:
        return ('Вам пора работать')
print(advice(18))
print(advice(10))
print(advice(6))
print(advice(0))
print(advice(55))

# Задание №2 (оператор IF)

def compare(a, b):
    if type(a) is str and type(b) is str:
        if a == b:
            return('1')
        elif a != b and len(a) > len(b):
            return('2')
        elif "learn" in b:
            return('3')
    else:
        return("0")

print(compare(1,"дом"))
print(compare("дом","дом"))
print(compare("дом","learn"))
print(compare("learn","learn"))
print(compare("домик","дом"))

# Задание №1 (оператор while)

def hello_user():
    while True:
        answer = input("Как дела? ")
        if answer == 'Хорошо':
            break
hello_user()

# Задание №2 (оператор while)

qa = {
    "Как дела?": "Позитив",
    "Как зовут?": "Питон",
    "Что делаешь?": "Отдыхаю"
    }

while True:
    ask_user = input("Что тебя интересует? ")
    if ask_user in qa.keys():
        print(qa.get(ask_user))
        break
    else:
        print ('Давай попробуем еще раз =)')

print ("---------")

 # Исключения задание №1
 
def hello_user():
    try:
        while True:
            answer = input("Как дела? ")
            if answer == 'Хорошо':
                break
    except KeyboardInterrupt:
        print("\nПока!")
        
hello_user()

# Исключения задание №2

def discounted(price, discount, max_discount = 30):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
        if max_discount >= 50:
            raise ValueError('Максимальная скидка не может быть больше 50%')
        if discount >= max_discount:
            price_with_discount = price
            return price
        else:
            price_with_discount = price - price * discount / 100
            return price_with_discount
    except (ValueError, TypeError):
        print("Не корректные данные")
        return " "

print(discounted(100,'десять'))
print(discounted(100,10))