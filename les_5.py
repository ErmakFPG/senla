while True:
    N = input('Введите количество слов: ')

    if not N.isdigit():
        print('Количество слов введено не корректно\n')
    elif int(N) > 100:
        print('Количество слов не должно превышать 100\n')
    else:
        words = input('Введите слова через пробел: ')
        word_list = words.split()
        if len(word_list) != int(N):
            print('Количество слов не совпадает с введенным количеством\n')
        else:
            word_list = words.split()
            word_list_mirror = [word for word in word_list if word == word[::-1]]
            print(f'Количество полиндромов: {len(word_list_mirror)}')
