from core.db import all_clients_data


def view_all_clients():
    if all_clients_data:
        for index in range(len(all_clients_data)):
            # for lists
            # print(f'{index+1}. {", ".join(all_clients_data[index])}')
            
            client_data = all_clients_data[index].values()
            print(f'{index + 1}. {", ".join(client_data)}')
    else:
        print('Няма регистрирани клиенти')
