number = int(input('Введите число: '))
count = 0
while  2 ** count <= number:
    print(2 ** count, end=' ')
    count += 1