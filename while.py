# Код внутри цикла выполняется раз за разом, пока условие не станет False
x = 1 
while x < 5:
    print(x)
    x += 1

print("---------")

# Цикл while становится бесконечным, если условие никогда не становится ложным.
# Ctrl + C прерывает бесконечный цикл

while True:
    user_say = input('Скажи что-нибудь: ')
    if user_say == 'Пока':
        print('Ну пока')
        break # цикл нужно завершить
    else:
        print('Сам ты {}'.format(user_say))

    