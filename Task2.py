while True:
    x = int(input("введите х: "))
    y = int(input("введите y: "))
    if x <= 1000 and y <= 1000:
        print(x,y)
        break
    else:
        print("введите число от 0 до 1000")
sum = x + y
p = x * y
print('сумма =' , sum)
print('произведение = ' , p)

while True:
    x1 = int(input("введите х1: "))
    y1 = int(input("введите y1: "))
    if sum == x1 + y1 and p == x1 * y1:
        print('молодец')
        break
    else:
        print('думай лучше')
            