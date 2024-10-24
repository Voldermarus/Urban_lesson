#1

my_dict = {"Иван" : 1956, "Сергей" : 1960, "Марина" : 1972}
print(my_dict)
print(my_dict["Сергей"])
print(my_dict.get("Николай"))
print(my_dict.get("Николай", "Имя в списке отсутствует"))
my_dict.update({"Виктор" : 1972, "Светлана" : 2001})
print(my_dict)
del my_dict["Сергей"]
print(my_dict)

# for i in sorted(my_dict):
#     print(i, my_dict[i])
#
# if input('') not in my_dict:
#     print('Имя не найдено')

# Полазил в Интернете. Это будет в дальнейших уроках?

#2

my_set = {1, 2, 3, 2, 2, 3}
print(my_set)
print(my_set.discard(2))
print(my_set)
my_set = {1, 2, 3, 2, 2, 3, "Помидор", (12, 25, "Вишня")}
print(my_set)
print(my_set.remove(3))
print(my_set)
print(my_set.add('Лимон'))
