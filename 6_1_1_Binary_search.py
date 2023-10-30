# Двоичный поиск чисел первого массива во втором массиве
# Вход: длина массива n (число) и сам массив числел (n чисел) в порядке возрастания, среди которых нужно вести поиск - записанные в строку и разделенные пробелом (строка)
#       длина массива k (число) и сам массив чисел (k чисел), которые нужно искать - записанные в строку и разделенные пробелом (строка)
# Выход: для каждого числа из второго массива - его позиция в первом массиве
#5 1 5 8 12 13
#5 8 1 23 1 11
#3 1 -1 1 -1

# Функция двоичного поиска
def binary_search(searched_array, searching_num, len_of_searched):      # на вход принимает массив (в котором нужно искать индексы), индекс (который нужно искать) и длину массива (в котором ищем индексы)
    left_edge = 0                                                       # левая граница поиска
    right_edge = len_of_searched - 1                                    # правая граница поиска
    # flag_find = False
    while left_edge <= right_edge:                                      # пока левая граница поиска меньше правой
        middle = left_edge + int((right_edge - left_edge) / 2)          # находим середину
        if searching_num == searched_array[middle]:                     # если элемент серидины поиска является искомым
            return middle+1                                             # возвращаем его индекс
        else:
            if searching_num < searched_array[middle]:                  # иначе, если искомое число располагается слева от середины поиска (то есть меньше)
                right_edge = middle - 1                                 # сдвигаем правую границу поиска
            else:                                                       # иначе, если искомое число располагается справа от середины поиска (то есть больше)
                left_edge = middle + 1                                  # сдвигаем левую границу поиска

    return -1


array_to_search = [int(k) for k in input().split()]                     # считываем первый массив
len_1 = array_to_search[0]                                              # сохраняем его длину
array_to_search.pop(0)                                                  # удаляем лишний элемент-длину

nums_for_searching = [int(k) for k in input().split()]                  # считываем второй массив
len_2 = nums_for_searching[0]                                           # сохраняем его длину
nums_for_searching.pop(0)                                               # удаляем лишний элемент-длину
nums_dict = {}                                                          # создаем словарь, в которому будут храниться ключи - элементы второго массива
                                                                        # ис будут соответствовать значения - совпадающие индексы первого

for i in nums_for_searching:                                            # для всех искомых чисел
    if i not in nums_dict:                                              # если числа еще нет в словаре
        s_index = binary_search(array_to_search, i, len_1)              # ищем его
        nums_dict[i] = s_index                                          # добавляем его ключ, и значение - индекс (полученный из функции двоичного поиска)

ans_list = []                                                           # сохраняем все полученные values-индексы из словаря в список ответов
for i in nums_for_searching:
    ans_list.append(nums_dict[i])                                       # для всех ответов - выводим их

#print(ans_list)
print(*ans_list)
#print(array_to_search)
#print(nums_for_searching)


