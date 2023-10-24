player_1, player_2 = input('Ваш ход: ').split(' ')
gesture: list = ('камень', 'ножницы', 'бумага')
if player_1 in gesture and player_2 in gesture:
    if player_1 == 'камень' and player_2 == 'ножницы' or player_1 == 'ножницы' and player_2 == 'бумага' or player_1 == 'бумага' and player_2 == 'камень':
        print('игрок 1 выиграл')
    elif player_1 == player_2:
        print('ничья')
    else: 
        print('игрок 2 выиграл')
else:
    print('Кажется Вы играете не в ту игру...')