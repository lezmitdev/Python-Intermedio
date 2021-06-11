def run():
# crear list de numeros al cuadrado  no divisibles de 3
#    list =[]
#    for i in range(11):
#        if(i%3!=0):
#            list.append(i**2)
        
#    print(list)

# Crear list comprehension de multiplos de 4  que a la vez   # tambien sean multiplos  de 6 y 9 hasta 5 digitos
    
    list=[i for i in range (1, 200) if i%4==0 and i%6==0 and i%9==0]
    print(list)
if __name__=='__main__':
    run()