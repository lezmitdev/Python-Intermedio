def divisors(num):
    try:
       if  num<0:
            raise ValueError("Ingrese un número positivo")
            divisors=[]
            for i in range(1,num+1):
                if num%i==0:
                    divisors.append(i)
            return divisors
    except ValueError as ve:
        return ve
        print(ve)

def run():
    try:

        num= int(input("Ingrese un número: "))
        print(divisors(num))
        print("Termino el programa")
    except ValueError:
        print("Debes ingresar un número entero")

if __name__=="__main__":
    run()