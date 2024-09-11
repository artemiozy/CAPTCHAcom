# Нужные Библиотеки
from tkinter import *
import random
from tkinter import messagebox
import os

# Объявление переменных
attempts = 0
code = ""

# Функция для создания рамок и линий
def outline():
    c.create_rectangle(80, 10, 240, 70, fill='lightblue')
    c.create_line(80, 20, 230, 50)
    c.create_line(85, 55, 180, 25)
    c.create_line(150, 10, 170, 70)
    c.create_line(100, 65, 240, 40)

# Функция для генерации случайной капчи
def generate():
    n = ""
    for _ in range(6):
        cap = random.randint(1, 3)
        if cap == 1:
            value = random.randint(97, 122)
            n += chr(value)
        elif cap == 2:
            value = random.randint(65, 90)
            n += chr(value)
        else:
            value = random.randint(48, 57)
            n += chr(value)
    return n

# Функция для обновления капчи
def refresh():
    ent_cap.delete(0, END)
    global code
    code = generate()
    outline()
    c.create_text(160, 40, text=code, font='calibri 28 bold')
    c.grid(row=3, column=10)

# Функция для проверки правильности введённой капчи и регистрационного номера
def check():
    global attempts
    chk = ent_cap.get()
    ent_cap.delete(0, END)
    global code
    reg = Regno_ent.get()

    if not (reg.isdigit() and (len(reg) == 8 or len(reg) == 5)):
        messagebox.showerror("ERROR", "Invalid registration number")
        Regno_ent.delete(0, END)
        refresh()
        return

    # Проверка совпадения введенной капчи
    if chk == code:
        messagebox.showinfo("SUCCESS", f"Registration number {reg} accessed successfully")
        Regno_ent.delete(0, END)
        refresh()
        attempts = 0
    else:
        attempts += 1
        messagebox.showerror("ERROR", f"Incorrect CAPTCHA entered. Attempts: {attempts}")
        refresh()  # Обновляем капчу после неверного ввода

# Функции для изменения стиля кнопки при наведении мыши
def on_enter(e):
    sub_btn.config(background='lightblue', foreground="red")

def on_leave(e):
    sub_btn.config(background='white', foreground='black')

# Основное окно программы
root = Tk()
root.geometry('450x290')
root.title("Login")

# Поле для ввода регистрационного номера
Reg_no = Label(root, text='Registration Number: ', font='calibri 15 bold')
Reg_no.grid(row=1, column=10, sticky=E)
Regno_ent = Entry(root)
Regno_ent.grid(row=1, column=11)
Regno_ent.insert(0, "12104288")  # Изначально заполненяем поле регистрационного номера

# Поле для ввода капчи
ent = Label(root, text='Enter the Captcha: ', font='calibri 15 bold')
ent.grid(row=4, column=10)
ent_cap = Entry(root)
ent_cap.grid(row=4, column=11)

# Кнопка "Login"
sub_btn = Button(root, text='Login', relief=RIDGE, height=2, width=10, bg='white', fg='black',
                 activebackground='blue', activeforeground='black', font='Times 10 bold', command=check)
sub_btn.place(x=180, y=160)
sub_btn.bind('<Enter>', on_enter)
sub_btn.bind('<Leave>', on_leave)

# Создание кнопки "Reload"
if os.path.exists("Reload.png"):
    img = PhotoImage(file="Reload.png")
    refresh_btn = Button(root, text="Refresh", relief=RIDGE, height=30, width=40, bg='white', image=img,
                         activebackground='lightblue', command=refresh)
else:
    refresh_btn = Button(root, text="Refresh", relief=RIDGE, height=2, width=10, bg='white',
                         activebackground='lightblue', command=refresh)
refresh_btn.grid(row=3, column=11)

# Создание окна для отображения
c = Canvas(root, height=80, width=240)
outline()
code = generate()
c.create_text(160, 40, text=code, font='calibri 28 bold')
c.grid(row=3, column=10)

# Запуск
root.mainloop()