# new_name: str = input('type name: ')

# greet_message = 'Hello, Bob!'

# # greet_message: str = (
# #     greet _message[:-3] + new_name
# # )
# greet_message: str = \
#     greet_message.replace('Bob', new_name)  #не на прямую заменяет
# print(greet_message)





# river: str = 'mmmmississippi'

# print(
#     'm'+river.lstrip('m')          #обрезать слева\справа
# )        






# river: str = 'https://site.com'

# print(
#     river.lstrip('https://')      #удалил 's' тоже, начиная слева, пока не встретит тот, который не относится к удаляемым
# )      



#норм работает
# words: str = 'dsa das das         '

# print(
#     words.split()    
# )   




# words: str = '<!---dsa das das---!>'
# print(
#     words.strip('<!>-').split()        #просто split не сработает, сначала убрать ненужное
# )





import string 

numbers:str = string.digits

word: str = 'hell123o b32ob ho312w ar3e y231ou'

# for n in numbers:
#     word = word.replace(n, '')    #пробежит строчку и заменит любые на ничего

# print(
#     word.replace(numbers, '')   #удалит только напрямую 0123456789 а не любые
# )


#варик номер 2
# _word: str = ''
# for ch in word:
#     if ch in numbers:
#         continue        #если в numbers, продолжаем чекать и search for normal letters
#     else:
#         _word +=ch      #если ch не в numbers записываем в итоговое слово
# word = _word
# del _word


# пустые
# _word:str = ''
# _sum: float = 0.0
# _prod: float = 1.0
# _list: list = []
# _set: set = set([])
# _dictionary: dict = {}



words: str = 'Hello Bob, are you a bob? BOB!!!' #заменить всех бобов

# words = words.lower().replace('bob', 'Mary')   #записать маленькими, заменить всех бобов
# print(words)

# print(
#     words.capitalize()    #все маленькие, первая большая
# )

# print(
#     words.upper()     #или lower: все большие или маленькие соответственно 
# )

#выводит индекс Боба
#words = words.lower().find('bob')
# print (words)


# words = words.lower()
# while True:
#     bob_index = words.lower().find('bob')
#     if bob_index == -1:    # -1   -- не найден
#         break
#     else:
#         words =(
#              words[:bob_index] + 'Mary' + words[bob_index+len('bob'):]
#         )
#         #break    #без брейка удалит всех бобов по очереди
# print(words)


