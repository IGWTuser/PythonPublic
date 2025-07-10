<!-- Задача: Удаление дубликатов -->
    Написать функцию 

    def remove_duplicates(nums: list[int]) -> list[int]:

    Функция получает список целых чисел nums и возвращает новый список, в котором:

    Сохранился исходный порядок элементов;

    Удалены все дубликаты — каждый элемент встречается только один раз.

<!-- Как запускать? -->
    Нужно запустить код и через пробелы ввести целые числа, вот промпт:

    ''' bash

    python3 RemoveDuplicates.py

<!-- Примеры: -->
1) 
Enter integer numbers separated by spaces: 1 1 1 3 3 2 4 5 5
numbers without duplicates: [1, 3, 2, 4, 5]

2) 
Enter integer numbers separated by spaces: 
numbers without duplicates: []

3) 
Enter integer numbers separated by spaces: 11 12 11 12 11 12 13
numbers without duplicates: [11, 12, 13]