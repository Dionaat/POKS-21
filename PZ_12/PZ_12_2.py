# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 3 – 8.
# дано четырёхзначное число. Проверить выссказывание: "данное число читается одинаково слева направо и наоборот"
# 4554
from tkinter import *
def proverka():
    x = chislo.get()
    if len(x) != 4:
        iotg['text'] = 'Выссказывание неверно'
        chislo.delete(0, END)
    elif x[0] == x[3] and x[1] == x[2]:
        iotg['text'] = 'Выссказывание верно'
        chislo.delete(0, END)
    else:
        iotg['text'] = 'Выссказывание неверно'
        chislo.delete(0, END)
root = Tk()
root.geometry('300x200')
root.config(bg='gray')
root.resizable(height=False,width=False)
root.title('Практическая работа 12 №2')
zadacha = Label(text='Дано четырёхзначное число. Проверить \n выссказывание: "данное число читается \n одинаково слева \
направо и наоборот"')
zadacha.grid(row=0, columnspan=2, stick='wens')
chislo_text = Label(root, text='Введите число : ')
chislo_text.grid(row=1, column=0, pady=5, stick='wens')
chislo= Entry(root)
chislo.grid(row=1, column=1, stick='wens', pady=5)
iotg = Button(text='Нажмите для проверки \n выссказывания.', bd=5, font=('Arial', 12), fg='gray',
              command= lambda : proverka())
iotg.grid(row=2, columnspan=2, stick='wens', padx= 5, pady=5)
root.grid_rowconfigure(0, minsize=60)
root.grid_rowconfigure(1, minsize=20)
root.grid_rowconfigure(2, minsize=100)
root.grid_columnconfigure(0, minsize=150)
root.grid_columnconfigure(1, minsize=150)
root.mainloop()
