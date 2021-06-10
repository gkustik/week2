from collections import Counter

phone = ['iphone', 'iphone', 'samsung', 'lg']

count = Counter(phone)
print(count)

print(count["iphone"])

text = "Программирование"
count = Counter(text)

print(count)

count = Counter(text.lower().replace(' ',""))

print(count)