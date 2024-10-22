
print(12+89-1)

num1 = 12
print(num1)
num2 = 89
print(num2)
num3 = 1
print(num3)
sum([num1,num2])
result = (sum([num1,num2]) - (num3))
print(result)

#1st program

result = 9 ** 0.5 * 5
print(result)
result = (9 ** 0.5 * 5)
print(result)
result = ((9 ** 0.5) * 5)
print(result)

#2st program

print(9.99 > 9.98)
print(1000 != 1000.1)

#3st program

print(2 * 2 + 2)
print(2 * (2+2))
print(2 * 2 + 2 == 2 * (2 + 2))

#4st program

name = ('123.456')
print(name[4])

# Сначала не понял логики и, каюсь, подсмотрел.
# В задании сказано:  "Дана строка '123.456'".

print(int(float('123.456') * 10) % 10)

# насколько я понял, таким способом можно выбирать любую цифру после запятой или сразу несколько цифр

print(int(float('123.456') * 100) % 10)
print(int(float('123.456') * 100) % 100)
print(int(float('123.456') * 1000) % 10)
