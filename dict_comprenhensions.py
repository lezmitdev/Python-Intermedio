import math

def run():

    mydict={i**3 for i in range(1,101) if i%3!=0}
#    print(mydict)
# Raiz cuadra de numeros     
    mydict2={i:math.sqrt(i) for i in range(1,101)}
    print(mydict2)
if __name__=='__main__':
    run()

