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

print(discounted(100,'десять'))