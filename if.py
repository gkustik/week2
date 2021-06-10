balance = -10

print(bool(balance < 0))  #Условный оператор приводит выражение, которое идет после if, к типу Bool. Если выражение дает True - то блок после if будет выполнен.

if balance < 0:
    print ("Пополни баланс")

print ("---------")

# проверяем мик условий
balance = 200
price = 200
print(bool(balance < 0 or balance < price))
if balance < 0 or balance < price:
    print ("Пополни баланс")
else:
    print ("Спасибо за покупку")

print ("---------")
# проверить несколько разных условий и в каждом отдельном случае принимать разные решения:

temperature = 0

if temperature <= 0:
    print('На улице холодно')
elif 1 <= temperature <= 14:
    print('На улице прохладно')
elif 15 <= temperature <= 25:
    print('На улице норм')
else:
    print('На улице тепло')

print ("---------")

# добавляем if внутрь функции

def weather(temperature):
    if temperature <= 0:
        return('На улице холодно')
    elif 1 <= temperature <= 14:
        return('На улице прохладно')
    elif 15 <= temperature <= 25:
        return('На улице норм')
    else:
        return('На улице тепло')

print(weather(-2))
print(weather(30))
print(weather(12))

print ("---------")

phone1 = {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1,'discount': 15}
phone2 = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0,'discount': 30}

def discounted(price, discount, max_discount=20, name=""):
    price = abs(float(price)) # abs значение по модулю, положительные числа
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError("Слишком большая скидка")
    if discount >= max_discount or "iphone" in name.lower():
        return price
    else:
        return price - (price * discount / 100)

print(discounted(200, 10,)) #проверка функции

apple_desc = discounted(phone1['price'], phone1['discount'], name=phone1['name'])
print(apple_desc)

android_desc = discounted(phone2['price'], phone2['discount'], name=phone2['name'])
print(android_desc)

print ("---------")

# Использование "отрицательного" условия, например скидка не дается, если у телефона нет названия

phone1 = {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1,'discount': 15}
phone2 = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0,'discount': 30}
phone3 = {'name': '', 'stock': 5, 'price': 40000.0,'discount': 10}

def discounted(price, discount, max_discount=20, name=""):
    price = abs(float(price)) # abs значение по модулю, положительные числа
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError("Слишком большая скидка")
    if discount >= max_discount or "iphone" in name.lower() or not name: #добавили отрицание, что имя пустое
        return price
    else:
        return price - (price * discount / 100)

apple_desc = discounted(phone1['price'], phone1['discount'], name=phone1['name'])
print(apple_desc)

android_desc = discounted(phone2['price'], phone2['discount'], name=phone2['name'])
print(android_desc)

noname_desc = discounted(phone3['price'], phone3['discount'], name=phone3['name'])
print(android_desc)