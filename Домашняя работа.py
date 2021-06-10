
cook_book = {}
with open('recept.txt', encoding='utf-8') as recept:
    while True:
        name = recept.readline().strip()
        if not name:
            break
        number = int(recept.readline().strip())

        ingridients= []
        for _ in range(number):
            quantity: int
            ingredient_name: str
            measure: str

            leg = recept.readline().strip()
            first_a = leg.index('|')
            a_split = leg[first_a:].split('|')
            a_split[0] = leg[:first_a] + a_split[0]
            a_split = [x.strip() for x in a_split]

            dic1 = {}
            dic1['ingredient_name'] = a_split[0]
            dic1['quantity'] = a_split[1]
            dic1['measure'] = a_split[2]
            ingridients.append(dic1)

        recept.readline().strip()
        cook_book[name] = ingridients

for key, value in cook_book.items():
    print(f'{key} : \n{value}\n')

def get_shop_list_by_dishes(dishes, person_count):

    list = []

    for key, values in cook_book.items():
        for val in dishes:
            if key == val:
                for value in values:
                    list.append(value)


    list_1 = []
    for dish in list:
        for dish2, val in dish.items():

            if dish2 == 'quantity':
               dic_0 = dict.fromkeys(['quantity'], int(val)* person_count)
            if dish2 == 'measure':
               dic_1 = dict.fromkeys(['measure'], val)
               dic_1.update(dic_0)
               list_1.append(dic_1)

    resultdict = []
    counter =0
    for dish in list:
        for dish2, val in dish.items():

            if dish2 == 'ingredient_name':
                dic_2 = dict.fromkeys([val], list_1[counter])
                resultdict.append(dic_2)
        counter += 1

    for dish_per in resultdict:
        for dish in dish_per:
            print(f'{dish}: {dish_per[dish]}')

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

import os
os.chdir(path="hw")
list_of_files = os.listdir(path=".")
list3 = []
counter = 0
dict_update ={}

for _ in range(3):
 with open(list_of_files[counter], encoding='utf-8') as f:
    lines = 0
    for line in f:
     lines = lines + 1
     dic_4 = dict.fromkeys([list_of_files[counter]], lines)
     dict_update.update(dic_4)
 counter +=1
list3.append(dict_update)

sorted_dict = {}
for key1 in list3:
    sorted_values = sorted(key1.values())
    for i in sorted_values:
        for k in key1.keys():
            if key1[k] == i:
                sorted_dict[k] = key1[k]
                break

with open("final.txt", "w", encoding='utf-8') as file:
    for key, values in sorted_dict.items():
      file.write(f'Имя файла: {key}\n'
                 f'Количество строк в нем:  {values}\n')