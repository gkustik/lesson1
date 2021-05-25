phones = ["iPhone Xs", 'Samsung 10s', "Xiaomi Mi8"]

phones.append('iPhone 6')

print(phones)

print(phones[0])

print(phones[1:3])

print(phones[-1])

print(phones[:2])

#Поиск индекса
print(phones.index('Samsung 10s'))

#Посчет количества элементов
print(phones.count("iPhone Xs"))

print(phones.count("iPhone 9"))

#Сортировка - для однотипных данных 
phones.sort()

print(phones)

#Оператор in

print('Samsung 9s' in phones)

#Удаление по индексу

del phones[3]

print(phones)

phones.remove('Xiaomi Mi8')

print (phones)