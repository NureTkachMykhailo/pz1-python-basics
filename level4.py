import requests

# 1. Класи "Книга" та "Книготека"
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print(f"Книгу додано до бібліотеки: {book.title} ({book.author})")

library = Library()
library.add_book(Book("Кобзар", "Тарас Шевченко"))
library.add_book(Book("Тіні забутих предків", "Михайло Коцюбинський"))

# 2. Робота з API
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users/2", timeout=5)
    data = response.json()
    print(f"Дані з API: {data['name']} ({data['email']})")
except Exception as e:
    print(f"Помилка підключення до API: {e}")

# 3. Швидке сортування (QuickSort)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(f"Відсортований масив: {quick_sort([23, 4, 17, 9, 31, 2, 15])}")
