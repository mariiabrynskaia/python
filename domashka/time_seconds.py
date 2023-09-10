def print_time (x: int | float):
    time = f'{x // 3600} час(а/ов) и {x % 3600 // 60} минут(а/ы)'
    return time


n = int(input('Введите число: '))
print(print_time(n))