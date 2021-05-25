# функции - print / len 
# создать функцию def_название_функции() 

#price = 100
#discount = 5
#price_with_dicount = price - price * discount / 100
#print(price_with_dicount)

# создаем функцию
def discounted(price, discount):
     price = abs(float(price)) # abs значение по модулю, положительные числа
     discount = abs(float(discount))
     if discount >=100:
         price_with_discount = price
     else:
         price_with_discount = price - price * discount / 100
     return price_with_discount

#p = discounted(100, 50)
#print(p)

product = {'name': 'Samsung S10', 'stock': 88, 'price': 50000, 'discount': 50}

#print(type(product))
#print(type(product['discount']))

product['with_discount'] = discounted(product['price'], product['discount'])

print(product)

#позиционные аргументы

def discounted(price, discount, max_discount = 50):
     price = abs(float(price))
     discount = abs(float(discount))
     max_discount = abs(float(max_discount))
     if max_discount >= 99:
         raise ValueError('Максимальная скидка не может быть больше 99%')
     if discount >= max_discount:
         price_with_discount = price
         return price
     else:
         price_with_discount = price - price * discount / 100
         return price_with_discount

print(discounted(100,60))

#p = discounted(100, 50)
#print(p)

#product = {'name': 'Samsung S10', 'stock': 88, 'price': 50000, 'discount': 100}

#print(type(product))
#print(type(product['discount']))

#product['with_discount'] = discounted(product['price'], product['discount'])

#print(product)