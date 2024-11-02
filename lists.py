# from audioop import reverse
#
# fruits = ["apple", "orange", "mango", "tomato", "grape"]
#
# # adding to a list
#
# fruits.append("berry")
# print(fruits)
#
# fruits.insert(1, "starfruit")
# print(fruits)
#
# fruits.extend(["coolfruit", "badfruit", "hotfruit"])
# print(fruits)
#
# fruits += ["tangerine", "melon"]
# print(fruits)
#
# fruits.remove("melon")
# print(fruits)
#
# my_garage = ["buick", "jeep", "dodge"]
# mechanic_shop = []
#
# popped_car = my_garage.pop(2)
# mechanic_shop.append(popped_car)
#
# print(my_garage)
# print(mechanic_shop)
#
# del fruits[0:3]
# print(fruits)
#
# fruits.sort(key=len)
# print(fruits)
#
# fruits.reverse()
# print(fruits)
#
# print(sorted(fruits))
#
# print(list(reversed(fruits)))
#
# fruits2 = fruits.copy()
# fruits2.append("guava")
# print(fruits2)
# print(fruits)
from copy import deepcopy
list_of_games = [[1, 2], [3, 4], [5, 6], [7, 8]]

list_of_games_copy = deepcopy(list_of_games)
list_of_games_copy.append([1, 9])

print(list_of_games, list_of_games_copy)
list_of_games_copy[0].append("forfeit")
print(list_of_games, list_of_games_copy)
