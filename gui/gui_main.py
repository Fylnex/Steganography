from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class GUI:
   root = Tk() # создание окна

   root.geometry("400x400", ) # ширина х высота
   root.title("Steganography") # название окна
   root.resizable(False, False) # не даем изменять размер окна

   # добавляем фрейм
   frame = Frame(
   root,
   padx=10,
   pady=10
   )
   frame.pack(expand=True)

   root.mainloop() # запуск окна
