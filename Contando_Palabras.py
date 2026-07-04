
def Contar_Palabras(Texto):
    Cant_Palabras = {}
    Palabra = ""
    Cant_Letras = 0
    for char in Texto:
        if char != " ":
            Palabra += char
            Cant_Letras += 1
            if Cant_Letras == len(Texto):
                if Palabra in Cant_Palabras:
                    Cant_Palabras[Palabra] += 1
                else:
                    Cant_Palabras[Palabra] = 1
        else:
            if Palabra in Cant_Palabras:
                Cant_Palabras[Palabra] += 1
            else:
                Cant_Palabras[Palabra] = 1
            Cant_Letras += 1
            Palabra = ""
    print(Cant_Palabras)
    
Contar_Palabras("Hola soy Tomas Gonzalez")
