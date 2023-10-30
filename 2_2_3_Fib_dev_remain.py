# Программа для нахождения целоцисленного остатка от деления n-того числа Фибоначчи на m
# Вход: номер числа Фибоначчи (число) и произвольный делитель (число)
# Выход: остаток от деления n-того числа Фибоначчи на m (число)

# Для решения задачи в первую очередь необходимо вычислить период Пизано для m (дело в том, что остатки от деления чисел Фибоначчи
# на произвольное число m периодически повторяются
def pizzano_period(m):
    fibbonaci_ex = 0                                    # генерируем нулевое число (предыдущее число)
    fibbonaci_new = 1                                   # генерируем первое число (новое число)
    counter = 0                                         # счетчик для подсчета длины периода
    periods = [0, 1]                                    # список для записи самого периода
    flag_find = False                                   # флаг остановки поисков
    while flag_find != True:
        counter += 1                                    # увеличиваем значение счетчика на 1
        fibbonaci_mid = fibbonaci_new                   # вспомогательная переменная для хранения числа
        fibbonaci_new = (fibbonaci_ex + fibbonaci_new)  # вычисляем новое число текущей итерации
        fibbonaci_ex = fibbonaci_mid                    # обновляем предыдущее число
        remains_1 = fibbonaci_ex % m                    # ищем остаток от деления на m предыдущего числа
        remains_2 = fibbonaci_new % m                   # ищем остаток от деления на m нового числа
        periods.append(remains_2)                       # добавляем остатки в список
        if (remains_1 == 0) and (remains_2 == 1):       # если встретили комбинацию [0, 1], значит период найден
            flag_find = True                            # поднимаем флаг
    periods.pop(-1)                                     # удаляем два лишних элемента [0, 1]
    periods.pop(-1)
    #print(len(periods))
    #if flag_find == True
    return counter, periods                             # возвращаем длину периода и сам период

# Пригодится функция вычисления n-того числа Фиббоначи
def fib(n):
    # put your code here
    fibbonaci_ex = 0
    fibbonaci_new = 1
    for i in range(n-1):
        fibbonaci_mid = fibbonaci_new
        fibbonaci_new = fibbonaci_ex + fibbonaci_new
        fibbonaci_ex = fibbonaci_mid
    if n == 0:
        return 0
    else:
        return fibbonaci_new

#Сама функция, ищущая остаток
def fib_mod(n, m):
    if m == 1:                          # если делитель это единица, то остаток от деления всегда будет нулевым
        return 0
    # if n == 0:
    #     return 0
    per, periods = pizzano_period(m)    # находим длину периода и сам период
    ost = n % per                       # находим остаток от деления номера числа Фибоначчи на длину периода - это будет индексом искомого остатка в списке периода
    print(periods)
    return periods[ost]                 # возвращаем результат - элемент списка с нужным индексом


def main():
    n, m = map(int, input().split())
    #n, m = 0, 4
    print(fib_mod(n, m))

    #print(fib(n)%m)

    #print(pizzano_period(2))

    #print(7291993184377412737043195648396979558721167948342308637716205818587400148912186579874409368754354848994831816250311893410648104792440789475340471377366852420526027975140687031196633477605718294523235826853392138525%55)
    # print(digits_det(1))
    # print(digits_det(12))
    # print(digits_det(123))
    # print(digits_det(1234))
    # print(digits_det(12345))
    # print(digits_det(123456))
    # print(digits_det(1234567))        832040 30


if __name__ == "__main__":
    main()