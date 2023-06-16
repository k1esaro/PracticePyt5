def fun (x, n):
    if n == 1 :
        return (x)
    if n!=1:
        return(x*fun(x, n-1))
x=int(input("Введите число = "))
n=int(input("Введите степень = "))
print (fun(x, n))
