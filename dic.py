# набор элементов в формате ключ: значение
product = {
    "name": 'iPhone Xs', 
    "stock": 5, 
    'price': 65000 
    } 
print(product)

#длинна словаря - количество элементов
print(len(product))

#добавить новый элемент в ключ словаря
product['stock'] = 10

print(product)

#добавление новых ключей
product['memory'] = 64

print(product)

#запрос ключа
print(product['memory'])

#словарь.get запрос по ключу без ошибки что ключа нет
print(product.get('name'))
print(product.get('discount'))

# создание ключей через .get
print(product.get('discount', '10%'))
print(len(product))

#удаление ключа
del product['stock']
print(product)

#объединение списков и словарей

phones = ["iPhone Xs", 'Samsung 10s', "Xiaomi Mi8"]
#product ['recomended'] = phones

product = {
    "name": 'iPhone Xs', 
    "stock": 5, 
    'price': 65000,
    'recomended': phones 
    } 

print(product)

#обращение к ключу списка
print(product['recomended'])
#обращение к элементу в списке
print(product['recomended'][2])

#добавление элемента в список внутри словаря
product['recomended'].append('iPhone 5')
print(product['recomended'])

#создание списка словарей
stock = [
    {'name': 'iPhone X', 'stock': 24, 'price': 65000, 'recomended': ['Samsung S10', "iPhone 11"]},
    {'name': 'Samsung S10', 'stock': 88, 'price': 50000, 'discount': 15000},
    {'name': 'iPhone 11', 'stock': 44, 'price': 105000}
]

print(stock)

# Чтение скобочек [] - означает что это список, {} - словарь, '' - элемент словаря

print(stock[0]['name'])

stock[0]['price'] = stock[0]['price'] + 10000

#строка 73 другой способ

stock[1]['price'] += 5000

print(stock[0])
print(stock[1])

#вложенные элементы внутри словаря

print(stock[0]['recomended'][1])

#проверка типов данных

print(type(stock))

print(type(stock[0]))
