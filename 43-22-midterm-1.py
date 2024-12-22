def fibo(n):
    x=0
    y=1
    fibo_list=[]
    if n==0:
        fibo_list.append(0)
        print("Invalid")
    else:
        fibo_list.extend([0,1])
        for i in range(0,n):
            z=x+y
            x=y
            y=z
            fibo_list.append(z)
        fibo_len=len(fibo_list)
        sum=0
        print("Fibonacci Series:",end=" ")
        for j in range(0,fibo_len-2):
            print(fibo_list[j],end=" ")
fibo(100)
