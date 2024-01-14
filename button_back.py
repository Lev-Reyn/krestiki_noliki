import tkinter as tk


def o(btn: tk.Button, lst: list, znak: str = 'O'):
    """ставит нолик"""
    btn.cget('text')
    btn.configure(text=znak)

