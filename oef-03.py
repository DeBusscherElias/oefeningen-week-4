vrienden = []

vriend = input('Geef de naam van een vriend of sluit af met een leeg veld')

while vriend != "":
    #opslaan in lijst
    vrienden.append(vriend)
    #opnieuw vragen
    vriend = input('Geef de naam van een vriend of sluit af met een leeg veld')

print(f"Dit zijn je vrienden: {vrienden}")