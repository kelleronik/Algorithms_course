# Программа реализует алгоритм сортировки подсчетом.
# Вход: число n элементов несортированного массива (строка)
#       n чисел от 1 до 10 через пробел - несортированный массив (строка)
# Выход: n чисел через пробел - отсортированный массив (строка)

# Тест вход:
# 5
# 2 3 9 2 9
# Тест выход:
# 2 2 3 9 9

def count_sort(uns_arr, uns_len):
    sub_arr = [0] * 11
    for i in range(uns_len):
        sub_arr[uns_arr[i]] += 1
    for i in range(1, len(sub_arr)):
        sub_arr[i] = sub_arr[i] + sub_arr[i - 1]
    sor_arr = [0] * uns_len
    for i in range(len(uns_arr) - 1, -1, -1):
        sor_arr[sub_arr[uns_arr[i]] - 1] = uns_arr[i]
        sub_arr[uns_arr[i]] -= 1
    return sor_arr


unsort_len = int(input())                           # принимаем длину массива
unsort_array = list(map(int, input().split()))      # принимаем массив
sorted_array = count_sort(unsort_array, unsort_len)
print(*sorted_array)
