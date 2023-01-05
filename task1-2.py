def food_book():
    with open('recipes.txt', 'r', encoding = 'utf8') as cook_book:
        global book
        book = {}
        for line in cook_book:
            dish_name = line.strip()
            book[dish_name] = []
            ingredient_count = cook_book.readline()
            for i in range(int(ingredient_count)):
                emp = cook_book.readline()
                ingredient, quantity, measure = emp.split('|')
                dinner = {'ingredient': ingredient, 'quantity': int(quantity), 'measure': measure.strip()}
                book[dish_name].append(dinner)
            cook_book.readline()
    print(book)
    return book
food_book()

def get_shop_list_by_dishes(dishes, person_count):
    for dish in dishes:
        for menu, ingredient in book.items():
            if dish in menu:
                print(dish)
                for ingredients in ingredient:
                    ingredients['quantity'] *= person_count
                    print(ingredients)

get_shop_list_by_dishes(['Утка по-пекински', 'Омлет'], 6)
