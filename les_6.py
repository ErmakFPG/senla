from operator import itemgetter


try:
    weight_limit = float(input('Введите грузоподьемность рюкзака: '))
    item_count = input('Введите количество предметов: ')

    if item_count.isdigit():

        item_count = int(item_count)

        items = []
        for i in range(item_count):
            item_name = input('Введите название предмета: ')
            item_cost = float(input('Введите стоимость предмета: '))
            item_weight = float(input('Введите массу предмета: '))
            items.append([item_name, item_cost, item_weight, item_cost / item_weight])

        sorted_items = sorted(items, key=itemgetter(3, 2), reverse=True)

        value_items = []
        for item in sorted_items:
            if item[2] <= weight_limit:
                value_items.append(item[0])
                weight_limit -= item[2]

        print(f'Эффективное заполнение рюкзака: {value_items}')

    else:
        print('Количество предметов должно быть целым положительным числом\n')

except ValueError:
    print('Введены некорректные данные\n')
