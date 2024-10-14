
cel =input("geben Sie eine Grad Zahl ein: ")
cel =float (cel)

z1= 1.8
z2= 32
z3= 5/9


def fahrenheit(GradCelsius):
    ret = GradCelsius * z1 + z2
    return ret

r =fahrenheit(cel)
print(cel,"Grad entsprechen",r, "Fahrenheit")

fahr= input("Wie viel Fahrenheit wollen Sie in Celsisus umrechnen? ")
fahr= float (fahr)

def celsius(fahrenheit):
    ret= (fahrenheit-z2)*z3
    return ret

r= celsius(fahr)
print(fahr,"Fahrenheit entsprechen",r, "Celsius")

