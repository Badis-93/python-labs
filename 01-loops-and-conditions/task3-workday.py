total_tasks = 0
took_call = False
hour = 1
while hour <= 8:
    print (hour, '-й час')
    tasks = int(input('Сколько задач решит максим? '))
    total_tasks += tasks
    if not took_call:
        call = int(input('Звонит жена. Взять трубку? (1 - да, 0 - нет): '))
        if call == 1:
            took_call = True
    hour += 1
print('Рабочий день закончился. Всего выполнено задач:', total_tasks)
if took_call:
    print('Нужно зайти в магазин')   
