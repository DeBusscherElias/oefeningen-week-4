nieuwe_lijst_getallen = []

for getal in range (1, 483, 13):
    nieuwe_lijst_getallen.append(getal)

print(f"{nieuwe_lijst_getallen}")

nieuwe_lijst_getallen.reverse()

del nieuwe_lijst_getallen[0]

nieuwe_lijst_getallen.remove(66)