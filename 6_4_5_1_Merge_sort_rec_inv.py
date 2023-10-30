# Программа сортирует входной массив по неубыванию а также выводит число инверсий в нем (меру неупорядоченности)
# Вход: размер массива n (число - строка) и сам массив (n чисел через пробел - строка)
# Выход: число инверсий (число)

# Функция слияния двух входящих массивов
def merge_arrays(array_left, array_right):              # получает на вход два массива
    inversions = 0                                      # начальное число инверсий массивов
    merged_array = []                                   # Слитый массив - сначала пустой
    left_counter = 0
    right_counter = 0
    while left_counter < len(array_left) and right_counter < len(array_right):    # пока оба не выше, чем индекс последнего элемента соответствующего массива
        if array_left[left_counter] <= array_right[right_counter]:                # если самый первый элемент левого массива меньше или равен самого первого элемента правого
            merged_array.append(array_left[left_counter])                         # добавляем в слитый массив самый первый элемент левого
            left_counter += 1                                                     # увеличиваем счетчик на 1
        else:
            merged_array.append(array_right[right_counter])         # добавляем в слитый массив самый первый элемент правого
            right_counter += 1                                      # увеличиваем счетчик на 1
            inversions += len(array_left) - left_counter            # число инверсий увеличивается на оставшуюся длину левого (именно столько элементов левого массива больше того, что только что был добавлен в слитый массив из правого)
    merged_array = merged_array + array_left[left_counter:] + array_right[right_counter:]
    return merged_array, inversions                     # возвращаем слитый массив и число инверсий, которое было найдено при слиянии входных двух массивов

# Рекурсивная функция сортировки массива
def merge_sort(unsorted_array):
    #inv_tot = 0

    if len(unsorted_array) == 1:                        # если во входном массиве всего 1 элемент, то его и возвращаем
        inv_tot = 0                                     # число инверсий одного элемента - нулевое
        return unsorted_array, inv_tot

    mid_of_arr = int(len(unsorted_array)/2)                                         # находим индекс среднего элемента
    merged_left, inv_left = merge_sort(unsorted_array[:mid_of_arr])                 # рекурсивно вызываем функцию сортировки для левого подмассива, сохраняем в переменную все количество инверсий в левом подмассиве
    merged_right, inv_right = merge_sort(unsorted_array[mid_of_arr:])               # рекурсивно вызываем функцию сортировки для правого подмассива, сохраняем в переменную все количество инверсий в правом подмассиве
    sorted_pt, inv_curr = merge_arrays(merged_left, merged_right)                   # сливаем левый и правый подмассивы, ищем количество инверсий на текущем шаге рекурсии
    inv_tot = inv_curr + inv_left + inv_right                                       # суммарное число инверсий на текущем шаге рекурсии - это сумма инверсий в левом и правом подмассивах и инверсии при слитии на текущем шаге рекурсии
    return sorted_pt, inv_tot                                                       # возвращаем слитый массив и число инверсий в подмассиве



unsort_len = int(input())                                                               # принимаем длину массива
unsort_array = list(map(int, input().split()))                                          # принимаем сам несортированный массив
# unsort_array = [int(i) for i in input().split()]                                      # альтернативная версия записи исходного массива
#unsort_array, sum_of_inversions = merge_sort(unsort_array, 0, unsort_len - 1)

# sum_of_inversions = [0]
unsort_array, sum_of_inversions = merge_sort(unsort_array)               # перезаписываем несортированный массив и сохраняем суммарное число инверсий

# for i in range(0, 4, 2):
#     print(i)

# print(unsort_len)
# print(unsort_array)                                                                     # выводим сортированный массив
print(sum_of_inversions)                                                                # выводим число инверсий
