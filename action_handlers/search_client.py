from core.db import all_clients_data


def search_client():
    print('Въведете критерий за търсене:\n'
          '1. Част от име\n'
          '2. ЕГН\n'
          '3. Години\n'
          '4. Телефонен номер')

    search_criteria = int(input())
    criteria = {
        1: 'name',
        2: 'egn',
        3: 'age',
        4: 'phone_number'
    }
    search_criteria = criteria[search_criteria]
    search_value = input()
    for client in all_clients_data:
        client_value = client[search_criteria]
        if search_value == client_value or search_value in client_value:
            print(', '.join(client.values()))

