


# import re


# def check_number(r):
#     if r == float or r == int:
#         return True
#     return False


while True:
    
    resposta = input('Manda um numiru:')
    try:
        resposta_float = float(resposta)
    
        if  type(resposta_float) == float and (resposta_float < 0 or resposta_float > 10):
            print('Nope!')
        elif type(resposta_float) == float and (resposta_float >= 0 and resposta_float <= 10):
            print('Muito q bem!')
            break     
    except:  
            print('É o quê?!')  
            
    
    
    
    # if check_number(r = resposta) == True and (resposta < 0 or resposta > 10):
    #         print('Nope!')     
    # elif check_number(r = resposta) == True and (resposta >= 0 and resposta <= 10):
    #         print('Muito q bem!')
    #         break
    # elif check_number(r = resposta) == False:
    #     print('É o q?')
        
                
        
