
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

