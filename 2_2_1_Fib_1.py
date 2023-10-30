# Программа вычисления n-того числа Фибоначчи
# Вход: номер числа Фибоначчи (число)
# Выход: само число Фибоначчи (число)

# Функция нахождения n-того числа Фибоначчи (по его номеру)
def fib(n):
    # put your code here
    fibbonaci_ex = 0                                    # генерируем нулевое число (предыдущее число)
    fibbonaci_new = 1                                   # генерируем первое число (новое число)
    for i in range(n-1):                                # повторяем n раз
        fibbonaci_mid = fibbonaci_new                   # вспомогательная переменная для хранения числа
        fibbonaci_new = fibbonaci_ex + fibbonaci_new    # вычисляем новое число текущей итерации
        fibbonaci_ex = fibbonaci_mid                    # обновляем предыдущее число
    return fibbonaci_new

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()