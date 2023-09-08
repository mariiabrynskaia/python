from import_this import*
#from import_this import RACE_DATA

# def count_winners (x: int | str | float | dict [int | str | float, int | str | float]) -> int | str | float | dict [int | str | float, int | str | float]:

#     for key in RACE_DATA.items():   
#         for key in RACE_DATA.get(key):
#             if 'FinishedPlace' <=3:
#                  return RACE_DATA.get(key)
#     return 'There is nothing'
newstring: str = []
#print(RACE_DATA.get(1))
for key, value in RACE_DATA.items():
    for key in range(1, 6):
        newstring.append(value)
        print(newstring(1))
        #if new_list[2] <=3:
        #    print(f'Призер {new_list(0)}, занял(а) {2} место')
        
    





# def count (x: int | str | float | dict [int | str | float, int | str | float]) -> int | str | float:

#     for key in RACE_DATA.items():
#         if key == 1:
#             for key, value in RACE_DATA.items():
#                 print(f'Победитель: {key} {value}')
#         elif 'FinishedPlace' == 2:
#             for key, value in RACE_DATA.items():
#                 print(f'Второе место: {key} {value}')
#         elif 'FinishedPlace' == 3:
#             for key, value in RACE_DATA.items():
#                 print(f'Третье место: {key} {value}')
# answer = count(RACE_DATA.keys)
# print (answer)