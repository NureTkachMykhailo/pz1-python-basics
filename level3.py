import datetime

# 1. Розрахунок віку
birth_year = 2006
current_year = datetime.date.today().year
print(f"Вік користувача: {current_year - birth_year} років")

# 2. Фільтрація парних чисел
def filter_even(values):
    return [v for v in values if v % 2 == 0]

print(f"Парні числа: {filter_even([3, 4, 7, 8, 10, 15, 22])}")

# 3. Клас "Калькулятор"
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def divide(self, a, b):
        return a / b if b != 0 else "Помилка: ділення на нуль"

calc = Calculator()
print(f"Додавання (7+9): {calc.add(7, 9)}")
print(f"Віднімання (20-6): {calc.subtract(20, 6)}")
print(f"Ділення (15/3): {calc.divide(15, 3)}")

# 4. Перевірка на паліндром
def is_palindrome(word):
    cleaned = word.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

print(f"'Казак' - паліндром: {is_palindrome('Казак')}")
