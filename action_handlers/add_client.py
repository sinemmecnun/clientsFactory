from core.db import all_clients_data
from core.validators import validate_name, validate_age, validate_egn, validate_iban, validate_phone_number
from core.db import save_client
from core.classes.Client import Client
import tkinter as tk


def validate_input(name, age, egn, iban, phone_number):
    client_data = {}

    if validate_name(name):
        client_data['name'] = name
    else:
        pass

    if validate_age(age):
        client_data['age'] = age
    else:
        pass

    if validate_egn(egn):
        client_data['egn'] = egn
    else:
        pass

    if validate_iban(iban):
        client_data['iban'] = iban
    else:
        pass

    if validate_phone_number(phone_number):
        client_data['phone_number'] = phone_number
    else:
        pass

    all_clients_data.append(client_data)
    # save_client(client_data)

    # client = Client(name, age, egn, iban, phone_number)


def add_client():
    def on_submit():
        # чете стойностите на данните въведени в текстовите полета
        name = entry_name.get()
        age = entry_age.get()
        egn = entry_egn.get()
        iban = entry_iban.get()
        phone_number = entry_phone_number.get()

        # подава данните към валидатор, който валидира и записва данните
        validate_input(name, age, egn, iban, phone_number)

        root.destroy()

    root = tk.Tk()
    root.title('Регистрация')
    root.geometry('350x300')

    label_name = tk.Label(root, text='Име')
    label_name.pack()

    entry_name = tk.Entry(root)
    entry_name.pack()

    label_age = tk.Label(root, text='Години')
    label_age.pack()

    entry_age = tk.Entry(root)
    entry_age.pack()

    label_egn = tk.Label(root, text='ЕГН')
    label_egn.pack()

    entry_egn = tk.Entry(root)
    entry_egn.pack()

    label_iban = tk.Label(root, text='IBAN')
    label_iban.pack()

    entry_iban = tk.Entry(root)
    entry_iban.pack()

    label_phone_number = tk.Label(root, text='Тел. номер')
    label_phone_number.pack()

    entry_phone_number = tk.Entry(root)
    entry_phone_number.pack()

    checkbox_vip = tk.Checkbutton(root, text='VIP', onvalue=1, offvalue=0)
    checkbox_vip.pack()

    button_submit = tk.Button(root, text='Запиши', width=20, height=2, command=on_submit)
    button_submit.pack(padx=10, pady=10)

    root.mainloop()
