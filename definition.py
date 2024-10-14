a= input("geben sie eine Zahl für a ein :")
b= input("geben Sie eine Zahl für b ein :")
x= input("geben Sie eine Zahl für x ein :")
a=float(a)
b=float(b)
x=float(x)

def myfunc_1(a, b, x):
    ret = a * b + x
    return ret

r=myfunc_1(a,b,x)
print("y=",r)
