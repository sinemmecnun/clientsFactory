from action_handlers.view_all_clients import view_all_clients


def delete_client():
    view_all_clients()
    client_to_delete = int(input('Въведете номер за изтриване: ')) - 1
    del all_client_data[client_to_delete]
    
