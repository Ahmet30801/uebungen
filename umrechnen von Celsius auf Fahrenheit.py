print("möchten Sie von Fahrenheit auf Celsius umrechnen oder von Celsius auf Fahrenheit")
var= input("wenn Sie von Fahrenheit auf auf Celsius umrechnen dann geben Sie eine 1 ein und wenn Sie von Celsius auf Fahrenheit dann geben Sie eine 2 ein ")
var= float(var)

if var==1:
   var2=input("geben Sie mir eine Zahl die ich in Celsius umrechnen")
   var2=float(var2)
   def celsius(fartocel):
       ergfar = fartocel*9/5+32
       return ergfar
   erg1=celsius(var2)

elif var==2:
    var3=input("geben Sie mir eine Zahl die ich in Fahrenheit umrechne")
    var3=float(var3)
    def celsius(celtofar):
        ergcel=celtofar-32(/1.8)
        return ergcel
    







