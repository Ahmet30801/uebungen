'''
print("geben Sie ihr alter ein")
alter= input()
alter = int(alter)
if alter >= 18:
    print("der User ist volljährig")
elif alter <= 10:
    print("der User ist minderjährig")
    print("du bist ja noch ein Kind")
else:
    print("der User ist minderjährig")
'''

'''
print("geben Sie eine Positive ganze Zahl ein")
zahl = input()
zahl = int(zahl)

if zahl >= 0:
    print("die Zahl ist Positiv")
else:
    print("die Zahl ist Negativ")

if zahl  % 2:
    print("die Zahl ist ungerade")
else:
    print("die Zahl ist gerade")
'''
print("geben Sie ein Jahr an")
Jahr = input()
Jahr = int(Jahr)

if Jahr % 400 == 0:
    print ("Das Jahr ist ein Schaltjahr")
elif Jahr % 100 == 0:
    print ("Das Jahr ist kein Schaltjahr")
elif Jahr % 4 == 0:
    print ("Das Jahr ist ein Schaltjahr")
else:
    print ("Das Jahr ist kein Schaltjahr")





