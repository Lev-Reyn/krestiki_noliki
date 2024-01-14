# # [
# #     [1, 2, 3],
# #     [4, 5, 6],
# #     [7, 8, 9]
# # ]
#
# # +-------+-------+-------+
# # |       |       |       |
# # |   1   |   2   |   3   |
# # |       |       |       |
# # +-------+-------+-------+
# # |       |       |       |
# # |   4   |   X   |   6   |
# # |       |       |       |
# # +-------+-------+-------+
# # |       |       |       |
# # |   7   |   8   |   9   |
# # |       |       |       |
# # +-------+-------+-------+
#
#
#
#
#
#
# def show(lst: list):
#     s = f"""
# +-------+-------+-------+
# |       |       |       |
# |   {lst[0]}   |   {lst[1]}   |   {lst[2]}   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   {lst[3]}   |   {lst[4]}   |   {lst[5]}   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   {lst[6]}   |   {lst[7]}   |   {lst[8]}   |
# |       |       |       |
# +-------+-------+-------+
#     """
#     print(s)
#
#
# lst = [1, 2, 3, 4, 'X', 6, 7, 8, 9]
# show(lst)
# a = input('vvedite nomer polya, vash zna: ')
#
# if lst[int(a) -1] == 'O' or lst[int(a) - 1] == 'X':
#     a = input('vvedite drugoy nomer polya, vash zna: ')
# else:
#     lst[int(a) - 1] = 'O'
#     show(lst)
# # +-------+-------+-------+
# # |       |       |       |
# # |   1   |   2   |   3   |
# # |       |       |       |
# # +-------+-------+-------+
# # |       |       |       |
# # |   4   |   5   |   6   |
# # |       |       |       |
# # +-------+-------+-------+
# # |       |       |       |
# # |   7   |   8   |   9   |
# # |       |       |       |
# # +-------+-------+-------+
#
# # lst = ['O', 2, 3, 4, 'X', 6, 7, 8, 9]
# # show(lst)
# # # +-------+-------+-------+
# # # |       |       |       |
# # # |   O   |   2   |   3   |
# # # |       |       |       |
# # # +-------+-------+-------+
# # # |       |       |       |
# # # |   4   |   X   |   6   |
# # # |       |       |       |
# # # +-------+-------+-------+
# # # |       |       |       |
# # # |   7   |   8   |   9   |
# # # |       |       |       |
# # # +-------+-------+-------+
import time

from test import del_x_o, robot
from vin import vin, nichya, X, O


def show(lst: list):
    s = f"""
+-------+-------+-------+
|       |       |       |
|   {lst[0]}   |   {lst[1]}   |   {lst[2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {lst[3]}   |   {lst[4]}   |   {lst[5]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {lst[6]}   |   {lst[7]}   |   {lst[8]}   |
|       |       |       |
+-------+-------+-------+
    """
    print(s)


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

show(lst)
a = input('vvedite nomer polya, vash znachenia: ')
while True:
    if lst[int(a) - 1] == O or lst[int(a) - 1] == X:
        a = input('vvedite drugoy nomer polya, vash znachenia, ибо поле уже занято: ')
    else:
        lst[int(a) - 1] = O
        show(lst)
        # проверить выиграл ли человек
        if vin(lst) == O:
            print('Ты выиграл')
            break
        if nichya(lst):
            print('ничья')
            break
        # ходит робот
        time.sleep(2)
        lst[robot(del_x_o(lst)) - 1] = X
        show(lst)
        if vin(lst) == X:
            print('Ты проиграл')
            break
        if nichya(lst):
            print('ничья')
            break
        # предлагаем человеку сходить
        a = input('vvedite nomer polya, vash znachenia: ')


