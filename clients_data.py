# Прочетете от конзолата данни за нов клиент - име и фамилия, години, ЕГН, IBAN, телефонен номер.
# Валидирайте въведените данни и ги запишете в списък:
# - името и фамилията да се прочетат по отделно, но да се конкатенират при запис в списъка. Да се провери, че не съдържат цифри
# - годините не могат да са отрицателно число и трябва да е число по-голямо от 0. За да може да бъде регистриран клиент,
# трябва да е на поне 18 години.
# - ЕГН - 10 цифри
# - IBAN - първите 2 символа да са букви, дължината може да е до 34 символа
# - телефонен номер - 10 цифри, трябва да е български номер - да започва с 089, 087, 088 или 098
# Изведете всички данни на клиента в следния формат, готов за експорт към csv:
# Име Фамилия,години,ЕГН,IBAN,телефонен номер
from core.db import all_clients_data
from core.validators import validate_name, validate_age, validate_egn, validate_iban, validate_phone_number

while True:

    client_data = []
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

    client_data.append(f'{name} {lastname}')

    while True:
        age = input('Въведете години: ')
        if validate_age(age):
            break

    client_data.append(age)
    # - ЕГН - 10 цифри

    while True:
        egn = input('Въведете ЕГН: ')
        is_egn_valid = validate_egn(egn)
        if is_egn_valid:
            break

    while True:
        iban = input('Въведете IBAN: ')
        is_iban_valid = validate_iban(iban)

        if is_iban_valid:
            break

    client_data.append(iban)

    while True:
        phone_number = input('Въведете телефонен номер: ')
        is_number_valid = validate_phone_number(phone_number)

        if is_number_valid:
            client_data.append(phone_number)
            break

    all_clients_data.append(client_data)

    check_stop_program = input("Натисни 1 за въвеждане на нов клиент, натисни 2 за изход")
    if not check_stop_program == '1':
        break


# 3.	Да се направи сортиране на данните на клиентите по следните начини:
# a.	По име, възходящо
# b.	По години, низходящо
# c.	По име първо и след това по години

all_clients_data.sort(key=lambda x: x[0])
print(all_clients_data)

all_clients_data.sort(key=lambda x: -int(x[1]))
print(all_clients_data)

all_clients_data.sort(key=lambda x: (x[0], x[1]))
print(all_clients_data)


def sort_function(x):
    return x[0]


sorted_list = sorted(all_clients_data, key=sort_function)
print(sorted_list)

sorted(all_clients_data, )
print(','.join(all_clients_data))


