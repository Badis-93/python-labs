x = int(input('Какая сумма вклада: '))
p = int(input('Какой ежегодный процент вклада: '))
y = int(input('Сумма порога: '))
years = 0
while x < y:
    x = x + (x * p) // 100
    years += 1
print('Количество лет для достижения порога:', years)