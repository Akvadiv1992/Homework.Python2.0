from random import randint

a = int(input("количество чисел в массиве n: "))
print()
array = [0] * a
for i in range(a):
    array[i] = randint(1, 100)
print('массив :',array)

print('максимально число: ', end=' ')
print(''.join((sorted([str(i) for i in array], reverse=True))))