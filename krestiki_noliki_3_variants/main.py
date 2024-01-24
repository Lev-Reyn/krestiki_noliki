from tkinter import *
from tkmacosx import Button
from button_back import *
from krestiki_noliki_3_variants.buttons import ButtonsVariantGame, ButtonsPole

window = Tk()
window.title('Крестики нолики')
geometry = WindowGeometry(window=window, window_geometry='725x600')
window.resizable(width=False, height=False)  # запрещаем изменять размер окна
label_title = Label(text='Выбери режим игры', background='cyan', font=('impact', 15), width=80)
label_title.grid(columnspan=6, column=0, row=0)

btn_variants_game = ButtonsVariantGame(label_title=label_title)
btn_variants_game.grid()
# btn_pole = ButtonsPole(label_title=label_title, var_game=btn_variants_game.var_game)
# btn_pole.grid()



window.mainloop()
