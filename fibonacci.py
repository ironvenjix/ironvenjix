def fib(n):
    if(n == 0):
     return 0
    elif(n == 1 or n == 2):
     return 1
    else: 
     return fib(n-1) + fib(n-2) 

n = int(input("enter the number of terms you want to print : "))
i = 0
for i in range(0,n):
    print(fib(i))
    i += 1
  
