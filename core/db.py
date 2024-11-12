all_clients_data = []
# начало на база данни

with open('./db/clients_data.txt', 'r') as clients_data:
    for single_client in clients_data:
        client = {}
        single_client = single_client.rstrip('\n')
        name, age, egn, iban, phone_number = single_client.split(', ')

        client['name'] = name
        client['age'] = age
        client['egn'] = egn
        client['iban'] = iban
        client['phone_number'] = phone_number

        all_clients_data.append(client)


def save_client(client_temp_data):
    with open('./db/clients_data.txt', 'a') as file:
        string_data = f"{client_temp_data['name']}, {client_temp_data['age']}, {client_temp_data['egn']}, " \
                      f"{client_temp_data['iban']}, {client_temp_data['phone_number']}\n"
        file.write(string_data)


def overwrite_data():
    with open('./db/clients_data.txt', 'w') as file:
        for client in all_clients_data:
            string_data = f"{client['name']}, {client['age']}, {client['egn']}, " \
                          f"{client['iban']}, {client['phone_number']}\n"
            file.write(string_data)
