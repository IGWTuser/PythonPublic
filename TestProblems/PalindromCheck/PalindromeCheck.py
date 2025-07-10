def is_palindrome(s: str) -> bool:
    # Убираем все пробелы и приводим к одному регистру
    s = s.replace(" ", "").lower()
    # Выводим сравнение с перевёрнутой строкой
    return s == s[::-1]
# Запросим ввод строки
s = input("s = ")
# Выводим палиндром ли это
print('It is palindrome?:'," ", is_palindrome(s))