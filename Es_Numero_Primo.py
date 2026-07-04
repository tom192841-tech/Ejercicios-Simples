
def Primo(Num):
    if Num % 2 == 0 and not Num == 2:
        print("No es primo")
        Numeros_Primos()
    else:
        print("Es primo")
        Numeros_Primos()
        
def Numeros_Primos():
    print("Numeros primos del 1 al 100")
    for num in range(1, 100):
        if num % 2 == 0 and not num == 2:
            pass
        else:
            print(num)
        
def Comienzo():
    num = input("Pon un numero primo a Comprobar: ")
    Primo(int(num))
    
Comienzo()