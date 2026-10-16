secret = 3
attempts = 0
while True:
    number = int(input('Загадайте число от 1 до 10: '))
    attempts += 1
    if number < secret:
        print('Число меньше, чем нужно. Попробуйте еще раз')
    elif number > secret:
        print('Число больше, чем нужно. Попробуйте еще раз')
    else:
        print('Вы угадали! Число попыток:', attempts)        
        break