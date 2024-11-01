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

#2

my_set = {1, 2, 3, 2, 2, 3, 'вишня'}
print(my_set)
my_set.add((248, 15, 44))
my_set.add('лимон')
print(my_set.discard(2))
print(my_set)



