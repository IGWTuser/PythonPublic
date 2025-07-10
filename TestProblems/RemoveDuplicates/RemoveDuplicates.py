def remove_duplicates(nums: list[int]) -> list[int]:
    # Задаём result как пустой список, чтобы пиотон не ругался, что функция может не выдать список 
    result = []
    # Если пользователь не ввёл числа, то выдаём пустой список в ответ
    if len(nums) == 0:
        return result
    # Если список, введённый пользователем, не пуст, то мы по порядку поэлементно проходим его и, в случае если такого элемента мы ещё не встречали, то добавляем его в конец 
    else:
        i = 0
        while i < len(nums):
            in_result = False
            for j in result:
                if nums[i] == j:
                    in_result = True 
                    break
            if not in_result:
                result.append(nums[i])
            i += 1
        return result
# Просим пользователя вводить целые числа через пробелы
nums_str = input("Enter integer numbers separated by spaces: " )
# Создаём из строки, полученной от пользователя, список из целых чисел, разделяя строку по пробелам
nums = [int(k) for k in nums_str.split()]
# Выводим в качестве результата список чисел без повторений и с сохранением порядка, в котором они встречались
print("numbers without duplicates:", remove_duplicates(nums))