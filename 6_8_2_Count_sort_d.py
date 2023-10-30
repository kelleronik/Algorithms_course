# Программа реализует алгоритм сортировки подсчетом для любых целых положительных чисел (и 0)
# Вход: число n элементов несортированного массива (строка)
#       n чисел - несортированный массив (строка)
# Выход: n чисел через пробел - отсортированный массив (строка)


# 11
# 1241 434 22 1234567 4234 12345 55 3 242 2 1
# 1 2 3 22 55 242 434 1241 4234 12345 1234567
#    4   3  2    4     5  2 1   3 1 1

# Функция подсчета разрядов каждого числа входного массива и максимального разряда
def digits_counter(arr):
    degrees_array = []                      # список разрядов, соответствующих числам входного списка
    max_dec = - 1                           # инициализируем переменную с максимальным разрядом
    for i in arr:                           # для каждого числа во входном массиве
        dig = -1                            # инициализируем переменную с результатом целочисленного деления
        degree = 0                          # степень десятки, на которую делится число при проверке
        while dig != 0:                     # пока результат целочисленного деления числа на 10^degree не равен 0
            degree += 1                     # наращиваем степень
            dig = i // (10**degree)         # считаем результат
        degrees_array.append(degree)        # добавляем очередное вычисленное значение разряда в массив
        if degree > max_dec:                # если вычисленное значение больше максимального
            max_dec = degree                # обновляем максимальное
    return max_dec, degrees_array           # возвращаем максимальный разряд и список всех разрядов

# Функция сортировки по разрядам входного массива
def digits_sort(arr):
    max_degree, array_of_degrees = digits_counter(arr)                          # для входного списка вычисляем максимальный разряд
    sorted_by_degrees_list = []                                                 # отсортированный по разрядам список
    various_degrees_list = [0] * max_degree                                     # пустой список (с различными разрядами)
    for i in range(max_degree):
        sorted_by_degrees_list.append([])                                       # список с различными разрядами заполняем пустыми списками по количеству различных разрядов
    for i in range(len(array_of_degrees)):                                      # для всех переданных чисел
        sorted_by_degrees_list[array_of_degrees[i] - 1].append(arr[i])          # раскидываем их по подспискам, порядковые номера которых соответствуют числу разрядов
        various_degrees_list[array_of_degrees[i] - 1] = array_of_degrees[i]     # отдельно формируем список с разрядами по возрастанию (если числа соответствуюшего разряда нет, то на его месте остается 0
    return sorted_by_degrees_list, various_degrees_list

# Функция сортировки чисел одного разряда
def unit_sort(uns_arr, deg_of_arr):                         # получает на вход список с числами одного разряда и их разряд
    uns_len = len(uns_arr)                                  # длина входного списка
    #sub_arr = [0] * 10
    if uns_arr == []:                                       # если полученный список пуст
        return []                                           # то возвращаем пустой список
    for j in range(0, deg_of_arr):                          # для всех разрядов проводим сортировку подсчетом
        sub_arr = [0] * 10                                  #
        for i in range(uns_len):
            sub_arr[((uns_arr[i] // (10**j)) - (uns_arr[i] // (10**(j + 1))) * 10)] += 1
        for i in range(1, len(sub_arr)):
            sub_arr[i] = sub_arr[i] + sub_arr[i - 1]
        sor_arr = [0] * uns_len
        for i in range(len(uns_arr) - 1, -1, -1):
            sor_arr[sub_arr[((uns_arr[i] // (10**j)) - (uns_arr[i] // (10**(j + 1))) * 10)] - 1] = uns_arr[i]
            sub_arr[((uns_arr[i] // (10**j)) - (uns_arr[i] // (10**(j + 1))) * 10)] -= 1
        uns_arr = sor_arr
    return sor_arr

# Функция быстрой сортировки, получает на вход список и возвращает его отсортированную версию
def sort_count(arr):
    s_b_d, v_d = digits_sort(arr)                           # вызываем функцию сортировки чисел поразрядно
    sorted_arr = []                                         # промежуточный список отсортированных чисел (состоит из списков отсортированных чисел одного разряда)
    final_arr = []                                          # финальный возвращаемый список
    for i in range(len(s_b_d)):                             # для всех разрядов
        sorted_arr.append(unit_sort(s_b_d[i], v_d[i]))      # сортируем числа одного разряда и добавляем их в список
    for i in sorted_arr:
        for j in i:
            final_arr.append(j)                             # из списка со списками формируем единый непрерывный список
    return final_arr

unsort_len = int(input())                           # принимаем длину массива
unsort_array = list(map(int, input().split()))      # принимаем массив
#sorted_array = count_sort(unsort_array, unsort_len)
sorted_array = sort_count(unsort_array)
print(*sorted_array)
