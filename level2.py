# 1. Середнє значення чисел
numbers_set = [7, 11, 18, 4, 20]
average_value = sum(numbers_set) / len(numbers_set)
print(f"Середнє значення {numbers_set}: {average_value}")

# 2. Квадрати чисел від 1 до 20
squares = [n**2 for n in range(1, 21)]
print(f"Квадрати чисел 1-20: {squares}")

# 3. Перевірка числа на простоту
def is_prime_number(n):
    if n < 2:
        return False
    for divisor in range(2, int(n**0.5) + 1):
        if n % divisor == 0:
            return False
    return True

test_number = 29
print(f"{test_number} просте число: {is_prime_number(test_number)}")

# 4. Обернення рядка
def reverse_text(text):
    return text[::-1]

print(f"Обернений рядок 'Харків': {reverse_text('Харків')}")
