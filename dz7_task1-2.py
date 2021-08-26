from collections import Counter

def get_cook_book(file):
    cook_book = {}
    with open(file, 'r', encoding='utf8') as f:
        for lines in f:
            food_name = lines.strip()
            ingredients_amount = int(f.readline().strip())
            ingredients_list = []
            for el in range(ingredients_amount):
                temp_dict = {}
                ingredient_name, quantity, measure = f.readline().strip().split('|')
                temp_dict['ingredient_name'] = ingredient_name
                temp_dict['quantity'] = int(quantity)
                temp_dict['measure'] = measure
                ingredients_list.append(temp_dict)
            f.readline()
            cook_book[food_name] = ingredients_list
        for key, val in cook_book.items():
            print(key, ':\n ', '\n  '.join(map(str, val)))
        print('==========================================================================================')
        print()
        return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    global ingridient
    shop_list = {}
    temp_list = []
    for dish in dishes:
        if dish in cook_book:
            for ingridient in cook_book[dish]:
                volume_ingredients = {}
                ingridient['quantity'] *= person_count
                ingredient_name = ingridient.get('ingredient_name')
                volume_ingredients['measure'] = ingridient.get('measure')
                volume_ingredients['quantity'] = ingridient.get('quantity')
                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = volume_ingredients
                else:
                    temp_list.append(ingredient_name)
        else:
            print(f'{dish} нет в меню')
            print()
    a = dict(Counter(temp_list))
    for key, val in a.items():
        volume_ingredients2 = {'measure': ingridient.get('measure'), 'quantity': (val + 1) * person_count}
        shop_list[key] = volume_ingredients2
    for key, val in shop_list.items():
        print(key,':', val)
    return shop_list




get_shop_list_by_dishes(['Фахитос', 'Омлет', 'Утка по-пекински', 'Омлет2', 'Омлет3', 'Омлет4'], 1, get_cook_book('recipes.txt'))

