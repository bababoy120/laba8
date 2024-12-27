def find_first_odd_pair(t):
    for i in range(len(t) - 1):
        if t[i] % 2 != 0 and t[i + 1] % 2 != 0:
            return (i, i + 1)  # Возвращаем индексы первой найденной пары
    return None  # Если пара не найдена

numbers = (1, 3, 2, 5, 7, 4)
result = find_first_odd_pair(numbers)

if result:
    print(f"Первая пара соседних нечетных чисел находится на индексах: {result[0]} и {result[1]}")
else:
    print("Пара соседних нечетных чисел не найдена.")
