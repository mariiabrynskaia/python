vivod = []
decrease = False

numbers = [int(value) for value in input('Enter your numbers: ').split(' ')]  #эту штуку я загуглила, потому что типизация не позволяла мне пройти дальше Ln6 :(
for i in range(1, len(numbers)):
    if numbers[i] - numbers[i-1] > 1:
        vivod.append(i)
    elif numbers[i] - numbers[i-1] <= 0:
        decrease = True
if len(numbers) < 2:
    print('Enter more than 2 numbers')
elif decrease == True:
    print('Your sequence should be increasing')
elif not vivod:
    print('Not found')
elif decrease == False and len(vivod) == 1:
    print(vivod[0])
else:
    print(vivod)