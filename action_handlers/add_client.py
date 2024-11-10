from core.db import all_clients_data
from core.validators import validate_name, validate_age, validate_egn, validate_iban, validate_phone_number


def add_client():
    client_data = {}
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


