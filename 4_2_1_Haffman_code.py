# Данная программа вычисляет коды Хаффмана для заданной строки и кодирует ее
# Вход: строка из последовательности букв (строка)
# Выход: число n различных букв и размер закодированной строки m (два числа), все буквы и их коды (m строк), Закодированная строка (строка)

# НАДЕЖНЫЙ ШАГ: вычислить частоту встречающихся букв и сформировать список, отсортированный по возрастанию для частот встречающихся букв
# далее - сформировать общий список с листами-буквами (и их частотой) и с вершинами (и их частотой)
# далее - пройтись по этому общему списку, подсчитывая количество вхождений в него отдельных букв-листов и формируя код для каждой буквы
# далее - сформировать закодированную строку и вывести все согласно условию


inp_string_list = list(input())             # считывание входной строки во входной список
list_of_counts = []                         # список с частотой встречающихся символов [[a, 2], [b, 4], [c, 2], [d, 1]]
unique_list = []                            # список уникальных букв
list_of_positions = []                      # список с позициями всех букв в исходногй строке
for i in inp_string_list:                   # для букв во входном списке
    if unique_list.count(i) == 0:           # если встречается новая буква
        unique_list.append(i)               # добавляем букву в список уникальных букв
        list_of_counts.append([i, 1])       # добавляем букву в список с частотой
    else:
        ind = unique_list.index(i)          # находим в списке с частотой нужный элемент (текущую букву)
        list_of_counts[ind][1] += 1         # увеличиваем значение частоты соотв. буквы на 1

len_of_uniques = len(list_of_counts)        # количество уникальных букв
worklist = list_of_counts.copy()            # рабочий лист, копируем лист частот
regularized_list = []                       # Упорядоченный список с исходными буквами с родителями исходных букв, с родителями родителей (то есть со всеми вершинами вплоть до корня)

#worklist.sort(key=lambda x: x[1])                   #comment it

# По мере записи новых элементов в упорядоченный список из исходного элементы извлекаются
for k in range(len_of_uniques, 2*len_of_uniques):           #-1 Пробегаем от n до (2*n-1)
    if (worklist != []):                                    # Если рабочий список не пуст
        worklist.sort(key=lambda x: x[1])                   # сортируем его по возрастанию по частоте символов
    min_name_0 = worklist[0][0]                             # берется первый элемент рабочего списка (символы)
    min_num_0 = worklist[0][1]                              # берется первый элемент рабочего списка (частота)
    regularized_list.append([min_name_0, min_num_0])        # добавление в упорядоченный список (минимального элемента)
    worklist.pop(0)                                         # извлечение самого первого элемента рабочего списка
    if len(worklist) > 1:                                   # если рабочий список не содержит только корень
        min_name_1 = worklist[0][0]                         # берется первый элемент рабочего списка (символы)
        min_num_1 = worklist[0][1]                          # берется первый элемент рабочего списка (частота)
        regularized_list.append([min_name_1, min_num_1])    # добавление в упорядоченный список (Следующего по минимальности элемента)
        worklist.pop(0)                                     # извлечение самого первого элемента рабочего списка
        worklist.append([min_name_0 + min_name_1, min_num_0 + min_num_1])   # добавление в рабочий лист составной литеры

continum = list_of_counts.copy()                            # копируем лист частот
continum.sort(key=lambda x: x[1])                           # сортируем лист частот повозрастанию
for i in range(len(continum)):
    continum[i] = continum[i][0]                            # оставляем лишь последовательность букв по возрастанию

binaries_list = []                                          # список со всеми вершинами и бинарными кодировками для них
bin_flag = 0                                                # бинарный флаг
for i in range(len(regularized_list)):                      # для каждой вершины (в т.ч. и листьев) в порядке возрастания ее частоты
    if bin_flag == 0:                                       # по очереди, сначала одно условие, потом другое
        binaries_list.append([regularized_list[i][0],'0'])  # задаем имя вершины и код для нее 0
        bin_flag = 1                                        # поднимаем флаг
    else:
        binaries_list.append([regularized_list[i][0],'1'])  # задаем имя вершины и код для нее 1
        bin_flag = 0                                        # поднимаем флаг

binaries_list.reverse()                                     # реверсим список вершин и их бинарных кодировок (одно число)
codes = []                                                  # список с кодами для каждой вершины
for i in range(len(continum)):                              # для каждого элемента в списке частот (в нем только листья)
    code = ''                                               # начинаем составлять код
    for j in range(len(binaries_list)):                     # для каждого элемента в списке вершин и их бинарных кодировок (одно число)
        if continum[i] in binaries_list[j][0]:              # Если лист связан с текущим элементом списка вершин и их бинарных кодировок (одно число)
            code = code + binaries_list[j][1]               # Составляем двоичный код для листа (постепенно наращиваем его). Так, самый часто встречаемый элемент будет иметь кодировку длиной 1 (а если таких элемента два, то кодировку длиной 1, а может и 2)
    codes.append([continum[i], code])                       # добавление элемента в список с кодами (['элемент-лист', 'код'])

'''
#print(list_of_counts.count(1))
print('inp_string_list = ', inp_string_list)
print('list_of_counts = ', list_of_counts)
print('worklist = ', worklist)
print('regularized_list = ', regularized_list)
print('continum = ', continum)
print('binaries_list = ', binaries_list)
print('codes = ', codes)
'''


#В первой строке выведите количество различных букв k, встречающихся в строке, и размер получившейся закодированной строки.
#В следующих k строках запишите коды букв в формате "letter: code".
#В последней строке выведите закодированную строку.
out_code_string = ''                                #inp_string_list.copy() - Закодированная выходная строка
for i in range(len(inp_string_list)):               # для i от 0 до длины входной строки
    for j in range(len(codes)):                     # для j от 0 до длины списка кодов
        if inp_string_list[i] == codes[j][0]:       # если найдено совпадение элемента исходной строки и элемента списка кодов
            out_code_string = out_code_string + codes[j][1] # то добавляем к закодированной строке код найденного элемента
            break                                   # и досрочно выходим из цикла

print(len(continum), len(out_code_string))          # выводим количество уникальных букв и длину выходной строки

for i in codes:
    #print(i[0], ': ', i[1])
    print(f'{i[0]}: {i[1]}')                        # выводим строки со всеми буквами и их кодами


print(out_code_string)                              # выводим закодированную строку
#aabbccddeeefff #gageafegbgcegcgdbgfggfd




'''
for k in range(len_of_uniques, 2*len_of_uniques-1):
    worklist.sort(key=lambda x: x[2])
    min_name_0 = worklist[0][0]
    min_num_0 = worklist[0][1]
    if len(min_name_0) == 1
        regularized_list.append(min_name_0)
    if len(worklist) > 1:
        min_name_1 = worklist[1][0]
        min_num_1 = worklist[1][1]
        if len(min_name_1) == 1
            regularized_list.append(min_name_1)
        worklist.pop(0)
        worklist.pop(0)
        worklist.append([min_name_0 + min_name_1, min_num_0 + min_num_0])
'''

