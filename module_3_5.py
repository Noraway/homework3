def get_multiplied_digits(number):
    if not number:
        return 1
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(40203)
print(result)
result = get_multiplied_digits(420)
print(result)

print()
# Когда я задала вопрос преподавателю, мне сказали, что на ввод должна даваться строка, а не число.
# Иначе 042 на ввод дает ошибку, т.к. тип int не может начинаться на 0, возникает ошибка синтаксиса.
# С таким определением задача будет выглядеть так:

def get_multiplied_digits_str(str_number):
    number = int(str_number)
    if not number:
        return 1
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits_str('40203')
print(result)
result = get_multiplied_digits_str('420')
print(result)
result = get_multiplied_digits_str('042')
print(result)
result = get_multiplied_digits_str('0042')
print(result)
