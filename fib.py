n=8
fib1=0
fib2=1
print(fib1)
print(fib2)
for i in range(2,n):
    fib3=fib1+fib2
    fib1=fib2
    fib2=fib3
    print(fib3)