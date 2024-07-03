calls = 0
def count_calls():
    global calls
    calls = 4

    print(calls)
def string_info(string):
    calls_4 = 'Capybara'
    calls_1 = 'Armageddon'
    print(len(calls_4), calls_4.upper(), calls_4.lower())
    print(len(calls_1), calls_1.upper(), calls_1.lower())
def is_contains():
    calls_2 = 'Urban'
    callS_3 = ['cucle']
    if calls_2 == 'urban':
        print(True)
    elif callS_3 == 'urban':
        print(False)

string_info(calls)
is_contains()
count_calls()


# print(string_info('Capybara'))
# print(string_info('Armageddon'))
# print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
# print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
# print(calls)

