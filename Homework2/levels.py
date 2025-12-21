print("каким уровнем хотите воспользоваться? 1 2 3 4")
begin = str(input())
if begin == '1':
    print("Напишите строку:")
    text = str(input())
    print('Выбирите метод: upper,lower, capitalize')
    method = str(input())
    print(level_one(method))
elif begin == '2':
    print("Напишите строку:")
    text = input()
    print('Выбирите метод:find, replace, count')
    method = input()
    print(level_two(method))
elif begin == '3':
    print("Напишите строку:")
    text = input()
    print('Выбирите метод: split, join')
    method = input()
    print(level_three(method))
def level_one(method:str) -> str:
    global text
    if method == 'upper':
        return text.upper()
    elif method == 'lower':
        return text.lower()
    elif method == 'capitalize':
        return text.capitalize()
def level_two(method:str) -> str:  # функция для операций find, replace, count
    global text
    if method == 'find':
        print('Введите слово, которое хотите найти')
        letter_find = input()
        return text.find(letter_find)
    elif method == 'replace':
        print('Введите слово, которое хотите заменить')
        letter_replace = input()
        print("Введите слово, на которое хотите заменить")
        letter_rereplace = input()
        text = text.replace(letter_replace, letter_rereplace)
        return text
    elif method == 'count':
        print('Введите символ, который хотите посчитать')
        count_letter = input()
        return text.count(count_letter)
def level_three(method:str) -> str: #функция для операций split, join
    global text
    if method == 'split':
        print('Введите символ (разделитель)')
        letter_split = str(input())
        return text.split(letter_split)
    elif method == 'join':
        print('Что хотите сделать?:paste, join_str')
        operation = str(input())
        if operation == 'paste':
            print("Напишите символ")
            letter_paste = str(input())
            return letter_paste.join(text)
        elif operation == 'join_str':
            print("Напишите строку, которую хотите присоединить к уже написанной")
            letter_join= str(input())
            return text.join(letter_join)
    elif method == 'count':
        print('Введите символ, который хотите посчитать')
        count_letter = str(input())
        return text.count(count_letter)
print(level_three(method))
def level_four(method:str) -> str: #функция для операций strip, isdigit, isalpha
    global text
    if method == 'strip':
        print('Введите символ')
        letter_strip = str(input())
        return text.strip(letter_strip)
    elif method == 'digits_or_symbols':
        if text.isdigit():
            return 'Текст состоит только из цифр'
        elif text.isalpha():
            return 'Текст состоит только из символов'
    elif method == 'hello':
        print('Введите имя человека')
        name = str(input())
        text_mail = 'Привет, {}!'.format(name)
        return text_mail
    elif method == 'bye':
        print('Введите имя человека')
        name_bye = str(input())
        text_bye = f'Пока, {name_bye}'
        return text_bye
print("каким уровнем хотите воспользоваться? 1 2 3 4")
begin = str(input())
if begin == '1':
    print("Напишите строку:")
    text = str(input())
    print('Выбирите метод: upper, lower, capitalize')
    method = str(input())
    print(level_one(method))
elif begin == '2':
    print("Напишите строку:")
    text = input()
    print('Выбирите метод: find, replace, count')
    method = input()
    print(level_two(method))
elif begin == '3':
    print("Напишите строку:")
    text = input()
    print('Выбирите метод: split, join')
    method = input()
    print(level_three(method))
elif begin == '4':
    print("Напишите строку или нажмите Enter")
    text = input()
    print('Выбирите метод: strip, digits_or_symbols, hello, bye')
    method = input()
