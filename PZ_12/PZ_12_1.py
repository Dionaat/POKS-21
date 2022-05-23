from tkinter import *

root = Tk()
root.title('Forms demo')
root.geometry('570x579+350+350')
root.resizable(width=False, height=False)
root['bg'] = '#ec3e1c'

Label(text='html5 forms demo', font='Calibre 40', bg='#ec3e1c', fg='white').place(x=80, y=13)
Frame(width=328, height=470, bg='#761f0c').place(x=128, y=104)

Label(text='First Name', bg='#761f0c', fg='white').place(x=147, y=109)
Frame(width=285, height=23, bg='red').place(x=149, y=128)  # делаю рамку позади поля ввода. Видится, как цвет границы
Entry(width=46).place(x=151, y=130)

Label(text='Last Name', bg='#761f0c', fg='white').place(x=147, y=167)
Frame(width=285, height=23, bg='red').place(x=149, y=187)
Entry(width=46).place(x=151, y=189)

Label(text='Email address', bg='#761f0c', fg='white').place(x=147, y=226)
Frame(width=285, height=23, bg='red').place(x=149, y=246)
Entry(width=46).place(x=151, y=248)

Label(text='Date of birthday (we like to send presents!)', bg='#761f0c', fg='white').place(x=147, y=285)
Spinbox(width=25).place(x=149, y=307)

Label(text='Country', bg='#761f0c', fg='white').place(x=147, y=344)
Entry(width=46).place(x=149, y=366)
Label(text='How many computers do you have at home?', bg='#761f0c', fg='white').place(x=147, y=403)
Spinbox(width=25).place(x=149, y=425)

Label(text="We love spam, and we'll share your email address with all our third-party friends.\n"
           "Heck, we'll even sell it! If you're happy to receive annoying email on a regular basis \n"
           "please click submit...\n\n"
           "denotes a required field",
      font='Arial 6',
      bg='#761f0c',
      fg='white',
      justify="left").place(x=149, y=470)

Button(text='Sign me up!', bg='#ff9600', fg='white', font='Arial 14', width=10).place(x=315, y=510)

root.mainloop()