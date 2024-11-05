

def choix_joueur():
    joueur1 = input("choisir soit (X) soit (O) :")
    while True:
        joueur1 = joueur1.upper()
        if joueur1 == "X":
            print("Vous avez choisi X. Le joueur 2 aura O")
            break
        elif joueur1 == "O":
            print("Vous avez choisi O. Le joueur 2 aura X")
            break
        else:
            joueur1 = input("choisir soit (X) soit (O) ")


choix_joueur()