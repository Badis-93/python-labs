number = int(input('Введите число: '))
count = 0
if number == 0:
    count = 1
else:
    while number > 0:
        number = number // 10
        count += 1
print('Количество цифр в числе:', count )        
