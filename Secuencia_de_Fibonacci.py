
def Fibonnacci():
    n0 = 0
    n1 = 1
    for num in range(1, 50):
         print(n0)
         n_fibo = n0 + n1
         n0 = n1
         n1 = n_fibo
         
Fibonnacci()