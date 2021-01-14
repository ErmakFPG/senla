def greatest_common_divisor(num1, num2):
    a = num1
    b = num2
    while a != b:
        if a > b:
            a, b = b, a
        b = b - a
    return a


while True:
    number1 = input('Введите первое целое число: ')
    number2 = input('Введите второе целое число: ')
    if number1.isdigit() and number2.isdigit() and int(number1) == float(number1) != 0 and \
            int(number2) == float(number2) != 0:
        number1 = int(number1)
        number2 = int(number2)
        gcd = greatest_common_divisor(number1, number2)
        lcm = int((number1 * number2) / gcd)
        print(f'Наименьшее общее кратное двух чисел {lcm}, наибольший общий делитель {gcd}\n')
    else:
        print('Ошибка ввода\n')
