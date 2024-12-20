def calculate_structure_sum(list_):
    sum = 0
    for i in list_:
        if isinstance(i, (int, float)):
            sum += i
        elif isinstance(i, str):
            sum += len(i)
        elif isinstance(i, (list, tuple, set)):
            sum += calculate_structure_sum(i)
        elif isinstance(i, dict):
            for key, value in i.items():
                if isinstance(key, (int, float)):
                    sum += key
                elif isinstance(key, str):
                    sum += len(key)
                if isinstance(value, (int, float)):
                    sum += value
                elif isinstance(value, str):
                    sum += len(value)
                elif isinstance(value, (list, tuple, set, dict)):
                    sum += calculate_structure_sum([value])
    return sum

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

# Другой пример 1: (результат - 107)
sample1 = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}]),
    {1: 1, 2: {'a': 1, 'b': 1}}
]

result = calculate_structure_sum(sample1)
print(result)
