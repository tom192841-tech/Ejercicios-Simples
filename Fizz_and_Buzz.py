
def Fizz_Buzz():
    for num in range(1,101):
        Div_3 = num % 3
        Div_5 = num % 5
        if Div_3 == 0 and Div_5 == 0:
            print("fizzbuzz")
        elif Div_3 == 0:
            print("fizz")
        elif Div_5 == 0:
            print("buzz")
        else:
            print(num)
    
Fizz_Buzz()