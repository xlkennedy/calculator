import os
import sys
import tkinter as tk
from tkinter import END
from PIL import Image, ImageTk


window = tk.Tk()
window.title('calculator')
window.geometry('500x300')
window.configure(bg = 'black')

if getattr(sys, 'frozen', False):
    folder = sys._MEIPASS
else:
    folder = os.path.dirname(os.path.abspath(__file__))
    
window.iconbitmap(os.path.join(folder, 'cx.ico'))

image_path = os.path.join(folder, 'unnamed.jpg')
image = Image.open(image_path)


image = image.resize((300, 300))
photo = ImageTk.PhotoImage(image)
labelph = tk.Label(window,
                   image=photo,
                   bd=0,
                   highlightthickness=0,
                   padx=0,
                   pady=0)
labelph.place(x=200, y=15)


entry1 = tk.Entry(
    window,
    font = ('Times New Roman', 16),
    fg = 'black')
entry1.place(x=230, y=20)

def zz():
    entry1.insert(tk.END, 0)
button0 = tk.Button(
    window,
    text = 0,
    font = ('Times New Roman', 16),
    fg = 'black',
    command = zz,
    bg = 'white')
button0.place(x=56, y=255)

def disable_typing(event):
    return "break"
entry1.bind('<Key>', disable_typing)


def q():
    entry1.insert(tk.END, 1)
button1 = tk.Button(
    window,
    text = 1,
    font = ('Times New Roman', 16),
    fg = 'black',
    command = q,
    bg = 'white')
button1.place(x=20, y=210)

def qw():
    entry1.insert(tk.END, 2)
button2 = tk.Button(
    window,
    text = 2,
    font = ('Times New Roman', 16),
    fg = 'black',
    command = qw,
    bg = 'white')
button2.place(x=56, y=210)

def qwe():
    entry1.insert(tk.END, 3)
button3 = tk.Button(
    window,
    text = 3,
    font = ('Times New Roman', 16),
    fg = 'black',
    command = qwe,
    bg = 'white')
button3.place(x=93, y=210)

def ds():
    entry1.insert(tk.END, 4)
button4 = tk.Button(
    window,
    text = 4,
    font = ('Times New Roman', 16),
    fg = 'black',
    command = ds,
    bg = 'white')
button4.place(x=20, y=160)

def dsa():
    entry1.insert(tk.END, 5)
button5 = tk.Button(
    window,
    text = 5,
    font = ('Times New Roman', 16),
    fg = 'black',
    command = dsa,
    bg = 'white')
button5.place(x=56, y=160)

def cxc():
    entry1.insert(tk.END, 6)
button6 = tk.Button(
    window,
    text = 6,
    font = ('Times New Roman', 16),
    fg = 'black',
    command = cxc,
    bg = 'white')
button6.place(x=93, y=160)

def fq():
    entry1.insert(tk.END, 7)
button7 = tk.Button(
    window,
    text = 7,
    font = ('Times New Roman', 16),
    fg = 'black',
    command = fq,
    bg = 'white')
button7.place(x=20, y=110)

def fe():
    entry1.insert(tk.END, 8)
button8 = tk.Button(
    window,
    text = 8,
    font = ('Times New Roman', 16),
    fg = 'black',
    command = fe,
    bg = 'white')
button8.place(x=56, y=110)

def fr():
    entry1.insert(tk.END, 9)
button9 = tk.Button(
    window,
    text = 9,
    font = ('Times New Roman', 16),
    fg = 'black',
    command = fr,
    bg = 'white')
button9.place(x=93, y=110)

def pll():
    entry1.insert(tk.END, '+')
plus1 = tk.Button(
    window,
    text = '+',
    font = ('Times New Roman', 16),
    fg = 'black',
    command = pll,
    bg = 'white')
plus1.place(x=130, y=210)

def minus():
    entry1.insert(tk.END, '-')
minuss = tk.Button(
    window,
    text = '-',
    width=2,
    font = ('Times New Roman', 14),
    fg = 'black',
    command = minus,
    bg = 'white')
minuss.place(x=130, y=160)

def zap():
    entry1.insert(tk.END, '.')
zapyataya = tk.Button(
    window,
    text = '.',
    width=2,
    font = ('Times New Roman', 14),
    fg = 'black',
    command = zap,
    bg = 'white')
zapyataya.place(x=93, y=255)
    

def umnozh():
    entry1.insert(tk.END, '*')
buttonu = tk.Button(
    window,
    text = '*',
    width=2,
    height=1,
    font = ('Times New Roman', 14),
    fg = 'black',
    command = umnozh,
    bg = 'white')
buttonu.place(x=130, y=110)

def delenie():
    entry1.insert(tk.END, '/')
buttondel = tk.Button(
    window,
    text = '/',
    width=2,
    font = ('Times New Roman', 14),
    fg = 'black',
    command = delenie,
    bg = 'white')
buttondel.place(x=130, y=65)

def procent():
    entry1.insert(tk.END, '%')
delproc = tk.Button(
    window,
    text = '%',
    font = ('Times New Roman', 14),
    fg = 'black',
    command = procent,
    bg = 'white')
delproc.place(x=93, y=65)

def calc():
    expression = entry1.get()
    result = eval(expression)
    
    entry1.delete(0, tk.END)
    entry1.insert(0, str(result))
calculate = tk.Button(
    window,
    text = '=',
    font = ('Times New Roman', 16),
    fg = 'black',
    command = calc,
    bg = 'white')
calculate.place(x=130, y=255)

def delt():
    entry1.delete(0, tk.END)
udalit = tk.Button(
    window,
    text = 'AC',
    width=2,
    font = ('Times New Roman', 14),
    fg = 'black',
    command = delt,
    bg = 'white')
udalit.place(x=56, y=65)

def delete_one():
    entry1.delete(len(entry1.get()) - 1, tk.END)
del_one = tk.Button(
    window,
    text = 'X',
    width=2,
    font = ('Times New Roman', 14),
    fg = 'black',
    command = delete_one,
    bg = 'white')
del_one.place(x=20, y=65)


def secret(event=None):
    entry1.delete(0, END)
    entry1.insert(0, 'Ира ❤')

window.bind_all("<Shift-C>", secret)


window.mainloop()