def is_even(num):
    if num % 2 == 0:
        return 'четное'
    return 'нечетное'


def is_simple(num):
    divider = 2
    while num > divider:
        if num % divider == 0:
            return 'составное'
        else:
            divider += 1
    return 'простое'


while True:
    number = (input('Введите целое число: '))
    if number.isdigit() and int(number) == float(number):
        number = int(number)
        print(f'Число {number} {is_even(number)} и {is_simple(number)}\n')
    else:
        print('Ошибка ввода\n')
