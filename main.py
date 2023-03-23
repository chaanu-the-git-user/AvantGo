from tkinter import *
from customtkinter import *
from win32api import GetSystemMetrics
hsh = GetSystemMetrics(0) / 2
app = CTk()
editor = Text(height=hsh, width=GetSystemMetrics(1))
editor.pack()
output = Text(height=hsh, width=GetSystemMetrics(1))
editor.pack()
app.mainloop()