#import module
#z = 12  + module.test


from module import greet
x = 42
def outer():
    #global y   #better to write nonlocal
    print ('y in outer before assig: {""y in locals()}')
    y =12
    def answer(x):
        
      return x
if __name__ =='__main__':
        x = 42
        print(
           f'y in main exists {"y" in locals()}'        #все переменные которые существуют щас в памяти и их можно достать ##globals -- не достать
        )