def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(7,'privet', 8)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = (6, 'goot', [89, 78, 97])
values_dict = {'a': 8,'b': 9,'c': 3}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = (8,'more')
print_params(*values_list_2,42)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
