print("geben Sie ihre Körpergewicht in kg an")
gewicht = input()
print("geben Sie ihre Körpergröße in m an")
groesse = input()
# hier folgt die Rechnung
bmi = float(gewicht) / float (groesse) ** 2
print("Ihr BMI beträgt:", bmi)