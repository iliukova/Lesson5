# Task 3
# Напишіть скрипт, який виводить цілі числа від 1 до 200,
# використовуючи цикл while. В одному рядку необхідно виведити лише п’ять цілих чисел. Наприклад,
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# ...

n = 1
while n in range(1, 201) and n < 200:
    j = 0
    while j < 5:
        print(n, end=" ")
        n += 1
        break
print()
