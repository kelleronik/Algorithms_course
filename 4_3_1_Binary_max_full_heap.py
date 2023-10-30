# Данная программа реализует очередь с приоритетами на основе полной двоичной max кучи
# Вход: число операций (число)
# Выход: извлеченные максимальные элементы (числа)

# Заводим функции вставки и извлечения, а также просеивания вверх (после вставки) и просеивания вниз (после извлечения)


def sift_up_BMFH(bmfh):                                                 # функция просеивания добавленного числа вверх, принимает на вход кучу с добавленным последним элементом
    flag_of_done = False                                                # флаг окончания просеивания
    length_of_BMFH = len(bmfh) - 1                                      # общая длина кучи
    index_of_up = length_of_BMFH                                        # текущий индекс просеиваемого элемента
    while flag_of_done == False:                                        # пока не поднят флаг окончания
        if index_of_up != 1:                                            # если элемент не поднялся в самй корень
            if bmfh[index_of_up] > bmfh[int(index_of_up / 2)]:          # если значение элемента больше его родителя
                save_var = bmfh[int(index_of_up / 2)]                   # меняем значения местами с использованием вспомогательной переменной
                bmfh[int(index_of_up / 2)] = bmfh[index_of_up]
                bmfh[index_of_up] = save_var
                index_of_up = int(index_of_up / 2)
            else:
                flag_of_done = True                                     # иначе поднимаем флаг, элемент на своем месте
        else:
            flag_of_done = True                                         # если элемент оказался в корне - поднимаем флаг, элемент на своем месте
    return bmfh

def sift_down_BMFH(bmfh):                                               # функция просеивания корня вниз
    flag_of_done = False                                                # флаг окончания просеивания
    length_of_BMFH = len(bmfh) - 1                                      # общая длина кучи
    index_of_down = 1                                                   # текущий индекс просеиваемого элемента
    while flag_of_done == False:                                        # пока не поднят флаг окончания
        if 2 * index_of_down <= length_of_BMFH:                         # если у элемента есть дети
            if 2 * index_of_down == length_of_BMFH:                     # если у элемента только один ребенок
                if bmfh[index_of_down] < bmfh[2*index_of_down]:         # если значение элемента меньше значения ребенка
                    save_var = bmfh[2 * index_of_down]                  # меняем значения местами с использованием вспомогательной переменной
                    bmfh[2 * index_of_down] = bmfh[index_of_down]
                    bmfh[index_of_down] = save_var
                    index_of_down = 2 * index_of_down
                else:                                                   # иначе поднимаем флаг, элемент на своем месте
                    flag_of_done = True
            else:                                                       # если у элемента два ребенка
                child_1 = bmfh[2 * index_of_down]                       # сохраняем значение первого ребенка
                child_2 = bmfh[2 * index_of_down+1]                     # сохраняем значение второго ребенка
                if child_1 > child_2:                                   # если значение превого ребенка больше, чем второго
                    if bmfh[index_of_down] < bmfh[2 * index_of_down]:   # если значение элемента меньше значения ребенка
                        save_var = bmfh[2 * index_of_down]              # меняем значения местами с использованием вспомогательной переменной
                        bmfh[2 * index_of_down] = bmfh[index_of_down]
                        bmfh[index_of_down] = save_var
                        index_of_down = 2 * index_of_down
                    else:                                                   # иначе поднимаем флаг, элемент на своем месте
                        flag_of_done = True
                else:                                                       # если значение второго ребенка больше, чем превого
                    if bmfh[index_of_down] < bmfh[2 * index_of_down + 1]:   # если значение элемента меньше значения ребенка
                        save_var = bmfh[2 * index_of_down + 1]              # меняем значения местами с использованием вспомогательной переменной
                        bmfh[2 * index_of_down + 1] = bmfh[index_of_down]
                        bmfh[index_of_down] = save_var
                        index_of_down = 2 * index_of_down + 1
                    else:                                                   # иначе поднимаем флаг, элемент на своем месте
                        flag_of_done = True
        else:                                                               # если у элемента нет детей, то заканчиваем просеивание вниз - элемент опустился максимально
            flag_of_done = True
    return bmfh

def insertion_BMFH(bmfh, n):                        # функция вставки, принимает на вход кучу и вставляемое число
    if bmfh == []:                                  # добавление костыля, если ранее он не был добавлен
        bmfh.append('crutch')
    bmfh.append(n)                                  # добавление числа последним элементом
    bmfh = sift_up_BMFH(bmfh)                       # вызов процедуры просеивания добавленного числа вверх
    return bmfh                                     # возвращение кучи с просеенным числом

def extraction_BMFH(bmfh):                          # функция вставки, принимает на вход кучу
    if bmfh == []:                                  # добавление костыля, если ранее он не был добавлен
        bmfh.append('crutch')
    if len(bmfh) > 1:                               # если куча не пуста
        max_of_BMFH = bmfh[1]                       # сохраняем максимум
        bmfh[1] = bmfh[-1]                          # на место корня ставим последний лист
        bmfh.pop(-1)                                # удаляем последний лист
        bmfh = sift_down_BMFH(bmfh)                 # вызов функции просеивания вниз для вставленного в корень листа
    else:
        print("Heap is empty")
        max_of_BMFH = None
    return max_of_BMFH, bmfh


bin_max_full_heap = ['crutch']                                                              # куча с костылем - заданным нулевым элементом для корректной работы ссылки на индексы
num_of_op = int(input())                                                                    # число операций
instructions = []                                                                           # список самих операций
command = ''                                                                                # текущая операция
maximums = []                                                                               # список извлеченных максимумов
for i in range(num_of_op):                                                                  # для каждой вводимой операции
    command = str(input())                                                                  # сохраняем ее в строку
    if "Insert" in command:                                                                 # если операция типа Вставка
        operation, number = (k for k in command.split(' '))                                 # отдельно записываем ее тип и число, которое будет вставлено
        instructions.append([operation, number])                                            # сохраняем в общий список операций
    if "ExtractMax" in command:                                                             # если операция типа Извлечение
        instructions.append("ExtractMax")                                                   # записываем ее тип

for i in range(num_of_op):                                                                  # для каждой введенной операции
    if isinstance(instructions[i], list):                                                   # если операция типа Вставка
        bin_max_full_heap = insertion_BMFH(bin_max_full_heap, int(instructions[i][1]))      # вызываем функцию вставки
        #print("Insertion of", int(instructions[i][1]), "done")
    else:                                                                                   # если операция типа Извлечение
        max_el, bin_max_full_heap = extraction_BMFH(bin_max_full_heap)                      # вызываем функцию вставки
        maximums.append(max_el)                                                             # сохраняем в список извлеченный максимум
        #print("Extraction of max done")

#print(bin_max_full_heap)
#print(instructions)
for i in maximums:                                                                          # для всех максимумов в списке
    print(i)                                                                                # выводим максимум







# def main():
#     bin_max_full_heap = []
#     num_of_op = int(input())
#     print(fib(num_of_op))
#     instructions = []
#     for iter in range(num_of_op):
#         operation, number = (k for k in input().split(' '))
#         instructions.append([operation, number])
#
#     print(instructions)
#
# if __name__ == "__main__":
#     main()