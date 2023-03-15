from random import randint

a = int(input("введите количество монет n: "))
print()
array = [0] * a
for i in range(a):
    array[i] = randint(0, 1)
print(array)
print()
count = 0
count_2 = 0
for i in range(len(array)):
    if array[i] == 1:
        count = count + 1
    else:
        count_2 = count_2 + 1
if count < count_2:
    print('необходимо перевернуть',count, 'монет')
else:    
    print('необходимо перевернуть',count_2, 'монет')