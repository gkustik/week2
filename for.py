#Цикл позволяет выполнить один и тот же набор действий действия несколько раз. Например, вот как можно напечатать "Привет мир!" 3 раза:
for number in range(3):
    print(f"Привет мир {number}!")

print("---------")

#перебрать строку по буквам
for letter in 'python':
    print(letter.upper())

print("---------")

# Разбить строку на слова и посчитать длину слов

example = "Я учусь писать код на Python"

for word in example.split():
    print(f'Длинна слова "{word}": {len(word)}')

print("---------")

# Цикл для списка или словаря

students_scores = {1, 21, 19, 6, 5}

print(f'Средняя оценка: {sum(students_scores)/len(students_scores)}')

for score in students_scores:
    print (score)

print("---------")

students_scores = {1, 21, 19, 6, 5}

print(f'Средняя оценка: {sum(students_scores)/len(students_scores)}')

# расчет средней оценки через цикл

scores_sum = 0
for score in students_scores:
    scores_sum += score
    print (scores_sum)

print(f'Средняя оценка: {scores_sum/len(students_scores)}')

print("---------")

# Цикл из словаря, для каждого из товара расчитываем скидку
