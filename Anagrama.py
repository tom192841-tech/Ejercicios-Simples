
def Anagrama(Primer_Palabra, Segunda_Palabra):
    print(f"Palabra a comprobar: {Primer_Palabra}")
    print(f"Palabra que me diste: {Segunda_Palabra}")
    print("Comprobando si es Anagrama")
    Lo_Formado = ""
    if not len(Primer_Palabra) == len(Segunda_Palabra):
        return False
    return sorted(Primer_Palabra) == sorted(Segunda_Palabra) 
    
        
print(Anagrama("Peppa", "Peppa"))

