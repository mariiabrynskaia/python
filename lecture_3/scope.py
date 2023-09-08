#import module
#z = 12  + module.test


# from module import greet
# x = 42
# def outer():
#     #global y   #better to write nonlocal
#     print ('y in outer before assig: {""y in locals()}')
#     y =12
#     def answer(x):
        
#       return x
# if __name__ =='__main__':
#         x = 42
#         print(
#            f'y in main exists {"y" in locals()}'        #все переменные которые существуют щас в памяти и их можно достать ##globals -- не достать
#         )


AGE_OF_CONSENT = 16
def do_stuff(x: str) -> str:
    return 'nothing'

if __name__ == '__main__':     #точка входа
    do_stuff(str(AGE_OF_CONSENT))