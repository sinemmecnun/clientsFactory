from core.db import clients_dict


# Решения на допълнителни задачи от упражнение 6
# сортиране по ключ
myKeys = list(clients_dict.keys())
myKeys.sort()

sorted_by_key = {i: clients_dict[i] for i in myKeys}
print(sorted_by_key)