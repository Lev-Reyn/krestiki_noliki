from tkinter import *
import sys
from tkmacosx import Button


# меняем корневую директорию (временное решение)
sys.path.insert(0, '/Users/levreyn/Yandex.Disk.localized/python_otr/крестики_нолики/krestiki_noliki')
from button_back import *
from krestiki_noliki_3_variants.buttons import ButtonsVariantGame, ButtonsServerClient

window = Tk()
window.title('Крестики нолики')
geometry = WindowGeometry(window=window, window_geometry='725x600')
window.resizable(width=False, height=False)  # запрещаем изменять размер окна
label_title = Label(text='Выбери режим игры', background='cyan', font=('impact', 15), width=80)
label_title.grid(columnspan=6, column=0, row=0)

btn_variants_game = ButtonsVariantGame(label_title=label_title, window=window)
btn_variants_game.grid()

# test = ButtonsServerClient(label_title=label_title)
# test.grid()

window.mainloop()

