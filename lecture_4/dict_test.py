#from typing import TypeAlias
#ComplicatedDict: TypeAllias = dict[int|str|None, int|str|None]
alphabet: dict[
    int|str|None|float,
    str|list|int|float|dict [int, str|int|dict]
    ] = {    #key in left, item in right. Item can be whatever
    1: 'A',
    2: 'B',
    3: set([1, 1, 2, 3, 5]),
    4: [1, 2],
    5: {
        1: 'B',
        2: 'SS'
    },
    10: 'Y',
    'Z': 10,
    0.1: 'SDA',
    True: 'sdasd',
    False: 123123,
    None: 'dasdas'
}

#print(alphabet[10])
#for pair in alphabet:                  #alphabet.values -> значения(буквы), alphabet.itmes -> pairs
   # print(pair)    #will print the keys(numbers)

# for key, value in alphabet.items():            # в key только int и str
#     if value in 'AY':       #только нужное значение
#       print(f'Ключ: {key} Значение: {value}')    #распакует отдельно индекс от значения



# O_letter = alphabet.get('0', None)
# if not O_letter:
#     print('No 0')


#вытаскиваем dictionary inside another dictionary:
print(alphabet.get(5))