from operator import attrgetter


class Item:
    def __init__(self, name, cost, weight):
        self.name = name
        self.cost = cost
        self.weight = weight
        self.value = cost / weight

    def add_in_backpack(self, backpack):
        return backpack.append(self.name)


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
            items.append(Item(item_name, item_cost, item_weight))

        sorted_items = sorted(items, key=attrgetter('value', 'weight'), reverse=True)

        value_items = []
        for item in sorted_items:
            if item.weight <= weight_limit:
                item.add_in_backpack(value_items)
                weight_limit -= item.weight

        print(f'Эффективное заполнение рюкзака: {value_items}')

    else:
        print('Количество предметов должно быть целым положительным числом\n')

except ValueError:
    print('Введены некорректные данные\n')
