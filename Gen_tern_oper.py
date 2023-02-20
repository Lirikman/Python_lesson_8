# 1. Написать свой генератор последовательностей, свой тернарный оператор

#  Последовательности кубов цифр
numbers = [10, 5, 1, 7, 4, 2, 6, 3, 8]
numbers_kub = [(i**3) for i in numbers]
print(numbers_kub)

# Последовательности чётных чисел от 1 до 100
eval_numbers = [i for i in range(1, 101) if i % 2 == 0]
print(eval_numbers)

# Последовательность факториалов от 1 до 10
from math import factorial
list_factorial = [factorial(i) for i in range(1, 11)]
print(list_factorial)

# Последовательность первых букв цветов, заглавными буквами
word = ['white', 'yellow', 'orange', 'green', 'black', 'brown', 'purple', 'pink']
color_code = [x[0].title() for x in word]
print(color_code)

# Множество состоящее из первых букв цветов, заглавными буквами
set_color = {i[0].title() for i in word}
print(set_color)

# Тернарный оператор, пример 1
number = 10
eval_number = True if number%2 == 0 else False
print(eval_number)

# Тернарный оператор, пример 2
number_1 = -54
abs_number = number_1 if number_1 >= 0 else abs(number_1)
print(abs_number)

# Тернарный оператор, пример 3
a, b = 23, 45
big_number = a if a > b else b
print(big_number)