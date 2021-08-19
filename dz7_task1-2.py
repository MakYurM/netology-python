def get_cook_book(file):
    cook_book = {}
    ingredients_list = []
    with open(file, 'r', encoding='utf8') as f:
        for lines in f:
            food_name = lines.strip()
            ingredients_amount = int(f.readline().strip())
            for el in range(ingredients_amount):
                ingredient_name, quantity, measure = f.readline().strip().split('|')
                ingredients_list.append(
                    {'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure}
                )
            f.readline()
            cook_book[food_name] = ingredients_list
        for key, val in cook_book.items():
            print(key, ':\n ', '\n  '.join(map(str, val)))
        return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    dict_1 = {}
    dict_2 = {}
    for key, val in get_cook_book('recipes.txt').items():
        for elem in dishes:
            if elem == key:
                for i in val:
                    ingredient_name = i.get('ingredient_name', None)
                    dict_1['measure'] = i.get('measure', None)
                    dict_1['quantity'] = i.get('quantity', None)
                    # print(ingredient_name, ':', dict_1)
                    dict_2[ingredient_name] = dict_1
                    for key, val in dict_2.items():
                        print(key, ':', val)


get_shop_list_by_dishes(['Утка по-пекински', 'Омлет'], 2)
