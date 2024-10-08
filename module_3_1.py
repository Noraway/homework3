calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    info = (len(string), string.upper(), string.lower())
    return info

def is_contains(string, list_to_search):
    count_calls()
    does_contain = False
    for i in range(len(list_to_search)):
        if list_to_search[i].lower() == string.lower():
            does_contain = True
    return does_contain

print(string_info('I hate rain'))
print(string_info('PINEapple'))
print(string_info('pineAPPLE'))
print(is_contains('Apple', ['Coconut', 'Banana', 'Tangerine']))
print(is_contains('Apple', ['apple', 'apricot', 'strawberry']))
print(calls)