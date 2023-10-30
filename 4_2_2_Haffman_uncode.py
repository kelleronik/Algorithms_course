# Данная программа считывает коды Хаффмана для заданной закодированной строки и раскодирует ее
# Вход: строка из последовательности букв (строка)
# Выход: число n различных букв и размер закодированной строки m (два числа), все буквы и их коды (m строк), Закодированная строка (строка)


symb_numb, code_len = (int(k) for k in input().split())         # количество букв и длина кодированной строки
codes = []                                                      # список с буквами и кодами
for i in range(symb_numb):
    symb, code = (k for k in input().split(": "))               # буквы и коды для них
    codes.append([symb, code])
codes.sort(key=lambda x: len(x[1]), reverse = False)            # сортируем коды по длине в порядке возрастания
coded_string =str(input())                                      # считываем закодированную строку

uncoded_string = ''                                             # раскодированная строка
stringing = ''                                                  # закодированная строка (кодирующая один символ)

for i in range(len(coded_string)):                              # для i от 0 до длины закодированной строки
    stringing = stringing + coded_string[i]                     # добавляем в строку один элемент (бинарный)
    for j in range(len(codes)):                                 # для всех элементов-кодировок
        if stringing == codes[j][1]:                            # если строка совпадает с элементом
            uncoded_string = uncoded_string + codes[j][0]       # то добавляем литеру этого элемента в раскодированную строку
            stringing = ''                                      # готовим строку к распознаванию следующего элемента
            break                                               # досрочно выходим из цикла


#print("codes =", codes)
#print("coded_string =", coded_string)
#print("uncoded_string =", uncoded_string)
print(uncoded_string)