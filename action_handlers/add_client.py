from core.db import all_clients_data
from core.validators import validate_name, validate_age, validate_egn, validate_iban, validate_phone_number
from core.db import save_client
from core.classes.Client import Client
import tkinter as tk


def add_client():
    client_data = {}

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

    button_submit = tk.Button(root, text='Запиши', width=20, height=2)
    button_submit.pack(padx=10, pady=10)

    root.mainloop()

    # следващата част ще се интегрира в диалога за регистрация и логиката за валидация ще се случва там
    while True:
        name = input('Въведете име: ')
        is_name_valid = validate_name(name)

        if is_name_valid:
            break

    while True:
        lastname = input('Въведете фамилия: ')
        is_lastname_valid = validate_name(lastname)

        if is_lastname_valid:
            break

    client_data['name'] = f'{name} {lastname}'

    while True:
        age = input('Въведете години: ')
        if validate_age(age):
            break

    client_data['age'] = age

    while True:
        egn = input('Въведете ЕГН: ')
        is_egn_valid = validate_egn(egn)
        if is_egn_valid:
            break
            
    client_data['egn'] = egn

    while True:
        iban = input('Въведете IBAN: ')
        is_iban_valid = validate_iban(iban)

        if is_iban_valid:
            break

    client_data['iban'] = iban

    while True:
        phone_number = input('Въведете телефонен номер: ')
        is_number_valid = validate_phone_number(phone_number)

        if is_number_valid:
            client_data['phone_number'] = phone_number
            break


    all_clients_data.append(client_data)
    save_client(client_data)

    client = Client(name, age, egn, iban, phone_number)



# all_clients_data.sort(key=lambda x: x[0])
# print(all_clients_data)
# 
# all_clients_data.sort(key=lambda x: -int(x[1]))
# print(all_clients_data)
# 
# all_clients_data.sort(key=lambda x: (x[0], x[1]))
# print(all_clients_data)
# 
# 
# def sort_function(x):
#     return x[0]
# 
# 
# sorted_list = sorted(all_clients_data, key=sort_function)
# print(sorted_list)
# 
# sorted(all_clients_data, )
# print(','.join(all_clients_data))


