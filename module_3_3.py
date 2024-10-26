def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(3, 4, 5)
print_params(2, 3, c = 1)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [3.3, 'string', False]
values_dict = {'a': 777, 'b': 'Hello!', 'c': None}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [39, 1.18]
print_params(*values_list_2, 42)