while True:
    text = input('Введите тест: ')
    key_word = input('Введите слово для поиска: ')

    text = text.lower().split()

    print(f'Количество слов в тексте: {text.count(key_word)}')
