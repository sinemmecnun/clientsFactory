from action_handlers.add_client import add_client
from action_handlers.view_all_clients import view_all_clients
from action_handlers.delete_client import delete_client
from action_handlers.search_client import search_client
from core.db import overwrite_data
from core.db import clients_dict


def initialize_program():
    while True:
        print('Изберете действие:\n'
              '1. Добави клиент\n'
              '2. Изтрий клиент\n'
              '3. Виж всички клиенти\n'
              '4. Търси клиент\n'
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
            overwrite_data()
            break
        else:
            print("Невалиден избор. Опитайте отново")
            
        print('Искате ли да продължите?\n'
              'y - yes or n - no')
        continue_program = input().lower()
        if continue_program != 'y':
            break

        print()


initialize_program()

# Решения на допълнителни задачи от упражнение 6
# сортиране по ключ
# myKeys = list(clients_dict.keys())
# myKeys.sort()
#
# sorted_by_key = {i: clients_dict[i] for i in myKeys}
# print(sorted_by_key)


# сортиране по име низходящо
sorted_by_values = dict(sorted(clients_dict.items(), key=lambda item: item[1]['name'], reverse=True))
print(sorted_by_values)
