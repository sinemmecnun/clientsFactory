from action_handlers.add_client import add_client
from action_handlers.view_all_clients import view_all_clients
from action_handlers.delete_client import delete_client
from action_handlers.search_client import search_client


def initialize_program():
    while True:
        print('Изберете действие:\n'
              '1. Добави клиент\n'
              '2. Изтрий клиент\n'
              '3. Виж всички клиенти\n'
              '4. Търси клиент по ЕГН\n'
              '5. Изход')

        action = int(input())
        if action == 1:
            add_client()
        elif action == 2:
            delete_client()
        elif action == 3:
            view_all_clients()
        elif action == 4:
            search_client()
        elif action == 5:
            break
        else:
            print("Невалиден избор. Опитайте отново")


initialize_program()