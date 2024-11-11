
input_data = open('input.txt', 'r') # открываем для чтения (литера 'r') файл и кладем его в переменую
data = input_data.read() # читаем другую переменую содержимое всего файла


# разбиваем строку в список (list) с использованием команды сплит (по умолчанию разделить - пробел)
data = data.split()
a = int(data[0]) # переменой а присваиваем значение первого элемента списка
b = int(data[1]) # переменой b присваиваем значение второго элемента списка
c = str(a+b) # считаем сумму и выполняем приведение к строке



output_data = open('output.txt', 'w') # открываем для записи (литера 'w') файл и кладем его в переменую
# записываем результат сложения и не забываем преобразовывать его в строку (иначе 
output_data.write(c)
# output_data.write(str(int(data[0]) + int(data[1])))

# ВАЖНО!!!
# не забываем закрывать открытые ранее файлы
input_data.close()
output_data.close()



import random

# Генерация списка из 100 случайных целых чисел
numbers = [random.randint(-100, 100) for _ in range(100)]

# Сортировка пузырьком
print("Сортировка пузырьком:")
сравнения_пузырька = 0
for i in range(len(numbers) - 1):
    for j in range(len(numbers) - i - 1):
        сравнения_пузырька += 1
        if numbers[j] < numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    print(f"Итерация {i + 1}: {numbers}")
print(f"Отсортированный список (пузырек): {numbers}")
print(f"Количество сравнений (пузырек): {сравнения_пузырька}")

# Сортировка выбором
print("\nСортировка выбором:")
сравнения_выбора = 0
for i in range(len(numbers) - 1):
    max_index = i
    for j in range(i + 1, len(numbers)):
        сравнения_выбора += 1
        if numbers[j] > numbers[max_index]:
            max_index = j
    numbers[i], numbers[max_index] = numbers[max_index], numbers[i]
    print(f"Итерация {i + 1}: {numbers}")
print(f"Отсортированный список (выбор): {numbers}")
print(f"Количество сравнений (выбор): {сравнения_выбора}")







import random

# Генерация отсортированного списка из 100 случайных целых чисел без дубликатов
numbers = sorted(random.sample(range(1_000_000), 100))

# Запрашиваем у пользователя число для поиска
target = int(input("Введите число для поиска: "))

# Линейный поиск
сравнения_linear = 0
for i, el in enumerate(numbers):
    сравнения_linear += 1
    if el == target:
        print(f"Элемент найден по линейному поиску на позиции {i} за {сравнения_linear} сравнений.")
        break
else:
    print(f"Элемент {target} не найден линейным поиском.")

# Бинарный поиск
сравнения_binary = 0
left = 0
right = len(numbers) - 1
while left <= right:
    сравнения_binary += 1
    mid = (left + right) // 2
    if numbers[mid] == target:
        print(f"Элемент найден по бинарному поиску на позиции {mid} за {сравнения_binary} сравнений.")
        break
    elif numbers[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print(f"Элемент {target} не найден бинарным поиском.")
