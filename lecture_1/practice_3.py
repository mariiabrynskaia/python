# n:int = int(input('Enter number '))
# def koren (x:int) -> int | float:
#      answer = x**(1/2)
#      return answer
# #print (koren(n))
# for i in range (1,n+1):
#     if n / i == i:
#         print(koren(n))
#         break
#     elif i>=n and n / i != i:
#         print('hard')




n = int(input('Enter number '))
def koren (x:int) -> int | str:

    for i in range (1,n+1):
        if n / i == i:
           return i
    return 'hard'
answer = koren(n)
print (answer)














# if koren(n) in array_kvadratov:
#     print(koren(n))
# else:
#     print('there is something wrong')
