def my_personal_sum(x: int | float, y: int | float) -> int | float:                #def от define (первое через: какой вводится, через стрелочку какой ожидается), | - или
#     #pass
     answer = x / y
     return answer
#     #или
#     #return x + y

# print(my_personal_sum(3, 5))
# print(sum([3, 5]))



# def my_personal_sum (
#         num_list: list
# ) -> int | float

# def my_personal_sum (
#         for num in num_list: 
#             answer += num)
#         return answer


# def my_personal_sum(*args, **kwargs) -> int | float:
#     print (f'Args: {args}')
#     print (f'Kwargs: {kwargs}')
#     answer = 0
#     for num in args:
#         answer += num
#         return answer
# print (my_personal_sum(3, 5, 1, 5, name = 'bob'))

print (my_personal_sum(y=2, x=1))