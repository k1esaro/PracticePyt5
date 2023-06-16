def sum (a,b):
    a+=1
    b-=1
    if b > 0:
        return sum(a,b)
    else:
        return a
a=int(input("1 число = "))
b=int(input("2 число = "))
print(sum(a,b))