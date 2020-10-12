def print_list(lijst):
    for item in lijst:
        print(f"op positie {lijst.index(item)} zit {item}")


verzameling1 = [12, 45, -9, -15]
verzameling2 = [12.23, 45.1, 9.478, 15.125, -3.14]
verzameling3 = ["Stijn", "Lies", "Henk"]

print_list(verzameling1)