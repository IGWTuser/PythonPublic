<!-- Задача: Анаграмы-->

    Написать функцию def are_anagrams(s1: str, s2: str) -> bool:

    Функция должна вернуть True, если строки s1 и s2 являются анаграммами друг друга, и False — в противном случае. Регистр букв и пробелы необходимо игнорировать.

    Анаграммы — это слова, которые состоят из одинаковых букв, но в разном порядке. При этом пробелы и регистр букв не учитываются.

<!-- Как запускать? -->

    Запустить код и ввести строки s1 и s2, вот промпт:

    '''bash
    python3 AnagramsCheck.py

<!-- Примеры:  -->

1)    
Enter s1: Listen
Enter s2: Silent
Are s1 and s2 are anagrams?: True

2) 
Enter s1: Hello
Enter s2: olelh       
Are s1 and s2 anagrams?: True

3) 
Enter s1: Python
Enter s2: Java
Are s1 and s2 anagrams?: False
