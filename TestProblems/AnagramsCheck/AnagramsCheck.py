def are_anagrams(s1: str, s2: str) -> bool:
    # Убираем в строках пробелы и делаем одинаковый регистр
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    # Переводим строки в множества
    s1_set = set(s1)
    s2_set = set(s2)
    # Если множества получились одинаковые (тогда их объединение и пересечение не должны друг от друга отличаться) выводим True, если разные, то выводим False. 
    if s1_set.union(s2_set) == s1_set.intersection(s2_set):
        return True
    else:
        return False
# Запрашиваем пользователя ввести строки    
s1 = input("Enter s1: ")
s2 = input("Enter s2: ")
# Выводим результат
print("Are s1 and s2 anagrams?:", are_anagrams(s1, s2))
