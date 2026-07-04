
def decimal_a_binario(Decimal):
    Num = Decimal
    Bin = ""
    while Num != 1:
        print(Num)
        Binario = int(Num) % 2
        print(Binario)
        Sig = int(Num) / 2
        Num = Sig
        Bin += str(Binario)
    Bin += str(1)
    Bin = Bin[::-1]
    print(Bin)
        
    
    
decimal_a_binario(2546)
    