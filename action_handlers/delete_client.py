from action_handlers.view_all_clients import view_all_clients
from core.db import all_clients_data


def delete_client():
    view_all_clients()
    client_to_delete = int(input('Въведете номер за изтриване: ')) - 1
    del all_clients_data[client_to_delete]
    
