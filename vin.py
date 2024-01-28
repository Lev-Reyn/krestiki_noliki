from typing import Union


X = 'X'  # для изменения цветов https://habr.com/ru/sandbox/158854/
O = 'O'


def vin(lst: list) -> Union[str, bool]:
    if lst[0] == lst[1] == lst[2]:
        if lst[0] == X:
            return X  # победить комп
        else:
            return O
    if lst[3] == lst[4] == lst[5]:
        if lst[3] == X:
            return X  # победить комп
        else:
            return O
    if lst[6] == lst[7] == lst[8]:
        if lst[6] == X:
            return X  # победить комп
        else:
            return O
    if lst[0] == lst[4] == lst[8]:
        if lst[0] == X:
            return X
        else:
            return O
    if lst[2] == lst[4] == lst[6]:
        if lst[2] == X:
            return X
        else:
            return O
    if lst[0] == lst[3] == lst[6]:
        if lst[0] == X:
            return X
        else:
            return O
    if lst[1] == lst[4] == lst[7]:
        if lst[1] == X:
            return X
        else:
            return O
    if lst[2] == lst[5] == lst[8]:
        if lst[2] == X:
            return X
        else:
            return O

    return False

    # return 'X' # победить комп
    # return 'O' # победить человек
    # return False # никто не победил


# def nichya(lst: list) -> bool:
#     if len(lst) == str:

# nichya([1, 2, "X", "X", "X", 6, 7, 8, 9])  # False
# nichya(["O", "O", "X", "X", "X", "O", "X", "X", "O"])  # True

def nichya(lst: list) -> bool:
    count = 0

    for i in range(len(lst)):
        if type(lst[i]) == str:
            count += 1
    if count == len(lst):
        return True
    return False


if __name__ == '__main__':
    # print(nichya(["X", 2, "X", "X", "X", 6, 7, 8, 9]))  # False
    # print(nichya(["O", "O", "X", "X", "X", "O", "X", "X", "O"]))  # True
    a = 'abobus'
    print('\033[35m' + a + '\033[0m')  # '\033[0m'
    print('тигран')
    print('lol')
