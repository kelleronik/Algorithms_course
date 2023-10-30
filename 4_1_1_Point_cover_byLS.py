# По данным n отрезкам необходимо найти множество точек минимального размера, для которого каждый из отрезков содержит хотя бы одну из точек
# Вход: количество отрезков (число) и сами отрезки (пары чисел)
# Выход: минимальное количество точек (число) и сами точки

# Задача сводится к перекрытию наименьшим числом точек наибольшего числа отрезков
# Сделать это можно, осортировав отрезки в первую очередь по левому краю, а во вторую по правому
# Каждая точка добавляется по правому краю первого отрезка в оставшемся списке
# Каждая добавляемая точка всегда должна перекрывать наибольшее число отрезков в отсортированном порядке (если выясняется, что точка поставлена слишком справа и не перекрывает
# "внутренний" отрезок для текущего, то при рассмотрении "внутреннего" отрезка она переносится левее - на правый его конец

#НАДЕЖНЫЙ ШАГ: расположить точку по правому краю отрезка, и в случае если следующие отрезки являются для него внутренними - смещать точку левее, ровняя по правому краю самого малого внутреннего

segment_numb = int(input())                                 # считывание числа отрезков
segments = []                                               # список с самими отрезками
for i in range(segment_numb):                               # записываем отрезки в список
    begining, ending = (int(k) for k in input().split())
    segments.append([begining, ending])

segments.sort(key = lambda x: x[1])                         # сортируем отрезки сначала по правому краю
segments.sort(key = lambda x: x[0])                         # затем сортируем отрезки по левому краю
# В результате получаем отсортированные в порядке возрастания отрезки по левому краю в первую очередь, и по правому краю во вторую

#print(segments)

points = [-1]

# точки добавляются слева направо, то есть последняя добавленная точка самая большая
segments_copy = segments.copy()                             # создаем копию списка на всякий случай
while len(segments) > 0:                                    # пока еще есть непокрытые точками отрезки
    # всегда рассматриваем первый отрезок из оставшихся - то есть находящийся левее всего (с минимальным правым краем)
    if segments[0][1] <= points[-1]:                        # если правый край отрезка меньше или равен, чем последняя добавленная точка (то есть можно было поставить предыдущую точку левее)
        points[-1] = segments[0][1]                         # то перезаписываем точку, как этот правый край
        segments.pop(0)                                     # удаляем отрезок
        continue                                            # переходим на следующую итерацию цикла
    if points[-1] < segments[0][0]:                         # если последняя добавленная точка меньше, чем левый край отрезка (то есть она не перекрывает текущий отрезок)
        points.append(segments[0][1])                       # то добавляем точку, как правый край отрезка
        segments.pop(0)                                     # удаляем отрезок
        continue                                            # переходим на следующую итерацию цикла
    if (segments[0][1] > points[-1]) and (points[-1] >= segments[0][0]):        # если последняя добавленная точка попала в первый отрезок из оставшихся (текущий), то удаляем его - он уже перекрыт
        segments.pop(0)                                     # удаляем отрезок


points.pop(0)                                               # удаляем лишнюю первую точку -1
print(len(points))                                          # выводим количество точек
print(*points)                                              # выводим сами точки



# То есть отрезки располагаются:
#     _______
#      _____
#        __________
#          _______
#            ___
#              ____
#              _____
#              _______
#                ________
#                          _______________
#                            _______
#                               ______________

# Точки будут располагаться, как показано "|"
#     _______
#      _____|
#        __________
#          _______
#            ___|
#              ____
#              _____
#              _______
#                ________|
#                          _______________
#                            _______|
#                               ______________