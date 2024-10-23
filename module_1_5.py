immutable_var = 1, 2, 3, 'мяч'
print(immutable_var)

mutable_list = ([5, 6, 7], 'лопата') + (12, 'лом')
print(mutable_list)

mutable_list = 5, 6, 7, 'лопата'
print(mutable_list)
mutable_list = [5, 6, 7], 'лопата'
print(mutable_list)
mutable_list[0][0] = "кирка"
print(mutable_list)
mutable_list = [5, 6, 7], 'лопата'
print(mutable_list)
mutable_list[0][2] = 'лом'
print(mutable_list)

# mutable_list = [5, 6, 7], 'лопата'
# print(mutable_list)
# mutable_list[0][3] = 'лом'
# print(mutable_list)

# Насколько я понял, можно заменять
# только элементы в квадратных скобках,
# что за ними, изменять нельзя. Выдает ошибку.

# mutable_list = [5, 6, 7, 'лопата']
# print(mutable_list)
# mutable_list[0][3] = 'лом'
# print(mutable_list)

# взяв в квадратные скобки весь список
# ни один из элементов невозможно заменить.
# Выдает ошибку.

# mutable_list = [5, 6, 7, 'лопата'],
# print(mutable_list)
# mutable_list[0][3] = 'лом'
# print(mutable_list)

# для того, что бы была возможность заменить элемент,
# после квадратных скобок ставим запятую, продолжив список.
# Что, наверное, является ошибкой.




