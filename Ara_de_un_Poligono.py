
def Calcular_Area(Figura):
    Figuras = ["Triangulo","Rectangulo","Cuadrado"]
    if Figura in Figuras:
        match Figura:
            case "Triangulo":
                print("Area = (base x altura) / 2")
            case "Rectangulo":
                print("Area = base x altura")
            case "Cuadrado":
                print("Area = lado x lado")
    else:
        print("Esa figura no es compatible")
        Comenzar()
    
def Comenzar():
    print("Figuras: Triangulo, Cuadrado, Rectangulo")
    Figura = input("Pon tu figura: ")
    Calcular_Area(Figura)
    
Comenzar()