#Задание №1 (список)
numbers = [3, 5, 7, 9, 10.5]
print(numbers)

numbers.append('Python')
print(numbers)

print(len(numbers))

#Задание №2 (список)
print(numbers[0])

print(numbers[-1])

print(numbers[1:6])

del numbers[5]

print(numbers)

#Задание №1 (словарь)
place = {'city': 'Москва', 'temperature':20}
print(place['city'])

place['temperature'] -= 3
place['temperature'] = place['temperature'] - 2
print(place)

#Задание №2 (словарь)
print(place.get('country'))
place ['country'] = "Россия"
place ["date"] = "27.05.2019"
print(place)
print(len(place))

#Задание №1 (функции)
def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    summ = one + delimiter + two
    print(summ.upper())
get_summ('Learn', 'python')

#Задание №2 (функция)
def format_price(price):
    price = int(price)
    print('Цена: {} руб.'.format(price))
format_price(56.24)