v1 = input()
v2 = input()
v3 = input()

if v1 == "vertebrado":
    if v2 == "ave":
        if v3 == "carnivoro":
            print("aguia")
        elif v3 == "onivoro":
            print("pomba")
    elif v2 == "mamifero":
        if v3 == "onivoro":
            print("homem")
        elif v3 == "herbivoro":
            print("vaca")
elif v1 == "invertebrado":
    if v2 == "inseto":
        if v3 == "hematofago":
            print("pulga")
        elif v3 == "herbivoro":
            print("lagarta")
    elif v2 == "anelideo":
        if v3 == "hematofago":
            print("sanguessuga")
        elif v3 == "onivoro":
            print("minhoca")
