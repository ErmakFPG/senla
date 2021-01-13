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
    number = float(input('Введите целое число: '))
    if int(number) == number:
        print(f'Число {int(number)} {is_even(number)} и {is_simple(number)}\n')
    else:
        print('Введенное число не целое\n')
