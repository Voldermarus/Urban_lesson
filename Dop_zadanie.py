my_dict = {}
grades = [[5, 3, 3, 5, 4],[2, 2, 2, 3], [4, 5, 5, 2], [4, 4,3], [5, 5, 5, 4, 5]]

grades_1 = grades[0]
grades_2 = grades[1]
grades_3 = grades[2]
grades_4 = grades[3]
grades_5 = grades[4]

grades1_sum = sum(grades[0])
grades2_sum = sum(grades[1])
grades3_sum = sum(grades[2])
grades4_sum = sum(grades[3])
grades5_sum = sum(grades[4])

grades1_len = len(grades_1)
grades2_len = len(grades_2)
grades3_len = len(grades_3)
grades4_len = len(grades_4)
grades5_len = len(grades_5)

result1 = (grades1_sum / grades1_len)
result2 = (grades2_sum / grades2_len)
result3 = (grades3_sum / grades3_len)
result4 = (grades4_sum / grades4_len)
result5 = (grades5_sum / grades5_len)

students = {'Jonny', 'Bilbo', 'Steve', 'Hendrik', 'Aaron'}
students = list(students)
students.sort()

name_1 = students[0]
name_2 = students[1]
name_3 = students[2]
name_4 = students[3]
name_5 = students[4]

my_dict[name_1] = result1
my_dict.update({name_2 : result2, name_3 : result3, name_4 : result4, name_5 : result5})
print(my_dict)

