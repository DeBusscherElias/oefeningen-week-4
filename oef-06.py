woord = input("Geef een woord op. >")

klinkers = []
medeklinkers = []

for letter in woord.lower():
    #if letter == "a" or letter == "e" or letter == "u" or letter == "o" or letter == "i" or letter == "y":
    if letter in ["a", "e", "o", "u", "y", "i"]:
        klinkers.append(letter)
    else:
        medeklinkers.append(letter)

print(f"Klinkers zijn: {klinkers}")
print(f"medeklinkers zijn: {medeklinkers}")