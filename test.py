import random


def del_x_o(lst: list) -> list:
    """Возвращает список без X и O"""
    lst_del = []
    for i in range(len(lst)):
        if type(lst[i]) != str:
            lst_del.append(lst[i])

    return lst_del


def robot(lst: list) -> int:
    """Выбирает куда ставить X"""
    return random.choice(lst)


if __name__ == '__main__':
    lst = [1, 2, 'O', 4, 'X', 6, 7, "X", "O"]
    lst_after_del_x_o = del_x_o(lst)
    print(robot(lst_after_del_x_o))
