while True:
    my_string = input('Введите строку с пробелами: ')
    word_list = my_string.split()
    word_count = len(word_list)
    my_string_sorted = ' '.join(sorted(word_list))

    my_string_upper = [el[0].upper() + el[1:] for el in word_list]
    my_string_upper = ' '.join(my_string_upper)

    print(f'Количество слов в строке: {word_count}')
    print(f'Отсортированный список: {my_string_sorted}')
    print(f'Строка с первыми заглавными буквами: {my_string_upper}\n')
