# 1. Виведення чисел від 1 до 10
for number in range(1, 11):
    print(number, end=" ")
print()

# 2. Привітання користувача
user_name = "Михайло"
print(f"Вітаю, {user_name}!")

# 3. Суматор двох чисел
value_a, value_b = 12, 30
print(f"Сума чисел {value_a} та {value_b}: {value_a + value_b}")

# 4. Пошук найменшого з трьох чисел
def smallest_of_three(x, y, z):
    return min(x, y, z)

print(f"Найменше число: {smallest_of_three(14, 3, 9)}")
