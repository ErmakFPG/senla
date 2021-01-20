def split_master(string, delimiter=' '):
    string_len = len(string)
    result = []
    start = 0
    for i in range(string_len):
        if string[i] == delimiter:
            result.append(string[start:i])
            start = i + 1

    result.append(string[start:string_len])

    return result


while True:
    my_string = input('Введите строку с пробелами: ')
    word_list = split_master(my_string)
    word_count = len(word_list)
    my_string_sorted = ' '.join(sorted(word_list))

    my_string_upper = [el[0].upper() + el[1:] for el in word_list]
    my_string_upper = ' '.join(my_string_upper)

    print(f'Количество слов в строке: {word_count}')
    print(f'Отсортированный список: {my_string_sorted}')
    print(f'Строка с первыми заглавными буквами: {my_string_upper}\n')
