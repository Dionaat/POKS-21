# Приложение ВЫДАЧА КРЕДИТОВ для некоторой организации. БД должна содержать таблицу Клиент со следующей
# структурой записи: ФИО клиента, ФИО сотрудника банка, срок кредита, процент кредита, сумма кредита.
# БД должна обеспечивать получение информации по сроку кредита.


import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):

    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#a0dea0', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        # self.add_img = tk.PhotoImage(file="BD/11.gif")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить игрока', command=self.open_dialog, bg='#5da130', bd=0,
                                    compound=tk.TOP)#, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        # self.update_img = tk.PhotoImage(file="BD/12.gif")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#5da130',
                                    bd=0, compound=tk.TOP)#, image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        # self.delete_img = tk.PhotoImage(file="BD/13.gif")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#5da130',
                                    bd=0, compound=tk.TOP)#, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        # self.search_img = tk.PhotoImage(file="BD/14.gif")
        btn_search = tk.Button(toolbar, text="Поиск записи", command=self.open_search_dialog, bg='#5da130',
                               bd=0, compound=tk.TOP)#, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        # self.refresh_img = tk.PhotoImage(file="BD/15.gif")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#5da130',
                               bd=0, compound=tk.TOP)#, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('klient', 'sotr', 'srok', 'proс', 'score'), height=15, show='headings')

        self.tree.column('klient', width=50, anchor=tk.CENTER)
        self.tree.column('sotr', width=180, anchor=tk.CENTER)
        self.tree.column('proс', width=140, anchor=tk.CENTER)
        self.tree.column('old', width=140, anchor=tk.CENTER)
        self.tree.column('score', width=140, anchor=tk.CENTER)

        self.tree.heading('klient', text='ФИО клиента')
        self.tree.heading('sotr', text='ФИО сотрудника')
        self.tree.heading('srok', text='Срок кредита')
        self.tree.heading('proс', text='Процент кредита')
        self.tree.heading('score', text='Сумма кредита')

        self.tree.pack()

    def records(self, klient, sotr, srok, proс, score):
        self.db.insert_data(klient, sotr, srok, proс, score)
        self.view_records()

    def update_record(self, klient, sotr, srok, proс, score):
        self.db.cur.execute("""UPDATE users SET klient=?, sotr=?, srok=?, proс=?, score=? WHERE klient=?""",
                            (klient, sotr, srok, proс, score, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM users""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM users WHERE klient=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    # def search_records(self, klient):
    #     klient = ("%" + klient + "%",)
    #     self.db.cur.execute("""SELECT * FROM users WHERE sotr LIKE ?""", klient)
    #     [self.tree.delete(i) for i in self.tree.get_children()]
    #     [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def search_records(self, score):
        score = (score,)
        self.db.cur.execute("""SELECT * FROM users WHERE score>?""", score)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]


    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()

class Child(tk.Toplevel):

    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить игрока')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Номер')
        label_description.place(x=50, y=25)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=110, y=25)

        label_sotr = tk.Label(self, text='Имя')
        label_sotr.place(x=50, y=50)
        self.entry_sotr = ttk.Entry(self)
        self.entry_sotr.place(x=110, y=50)

        label_sex = tk.Label(self, text='Пол')
        label_sex.place(x=50, y=75)
        self.combobox = ttk.Combobox(self, values=[u'Мужской', u'Женский'])
        self.combobox.current(0)
        self.combobox.place(x=110, y=75)

        label_old = tk.Label(self, text='Возраст')
        label_old.place(x=50, y=100)
        self.entry_old = ttk.Entry(self)
        self.entry_old.place(x=110, y=100)

        label_score = tk.Label(self, text='Результат')
        label_score.place(x=50, y=125)
        self.entry_score = ttk.Entry(self)
        self.entry_score.place(x=110, y=125)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                       self.entry_name.get(),
                                                                       self.combobox.get(),
                                                                       self.entry_old.get(),
                                                                       self.entry_score.get()))

        self.grab_set()
        self.focus_set()

class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=170)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          self.entry_name.get(),
                                                                          self.combobox.get(),
                                                                          self.entry_old.get(),
                                                                          self.entry_score.get()))
        self.btn_ok.destroy()

class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск")
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

class DB:
    def __init__(self):

        with sq.connect('BD/vidacha.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
                klient INTEGER PRIMARY KEY AUTOINCREMENT,
                sotr TEXT NOT NULL,
                srok INTEGER NOT NULL DEFAULT 1,
                proс INTEGER,
                score INTEGER
                )""")

    def insert_data(self, klient, sotr, srok, proс, score):
        self.cur.execute("""INSERT INTO users(klient, sotr, srok, proс, score) VALUES (?, ?, ?, ?, ?)""",
                             (klient, sotr, srok, proс, score))
        self.con.commit()

if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Работа с базой данных ВЫДАЧА КРЕДИТОВ")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()