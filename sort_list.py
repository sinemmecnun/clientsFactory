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