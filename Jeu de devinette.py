# import seed et randint de la librairie random
from random import seed
from random import randint

# définir la borne_minimale et la borne_maximale
borne_minimale = 0
borne_maximale = 1000


# fonction du  jeu de devinette
def devinette():
    # définir le nb_essais
    nb_essais = 0

    # choisi un nombre entre 0 et 1000 et défini value avec ce nombre
    seed()
    value = randint(borne_minimale, borne_maximale)

    # demande au joueur un chiffre entre 0 à 1000 et défini guess avec
    guess = int(input(
        f"J’ai choisi un nombre au hasard entre {borne_minimale} et {borne_maximale}.  À vous de le deviner... "
        f"\nEntrez votre essai :_"))

    # crée une boucle
    for i in range(0, 1000):

        # si la guess est plus petit que value
        if guess < value:
            # demande un nouvelle essai et augement par 1 nb_essais
            guess = int(input(f"Mauvaise réponse, le nombre est plus grand que {guess} \nEntrez votre essai :_"))
            nb_essais += 1

        # si la guess est plus grand que value
        elif guess > value:
            # demande un nouvelle essai et augement par 1 nb_essai
            guess = int(input(f"Mauvais choix, le nombre est plus petit que {guess} \nEntrez votre essai :_"))
            nb_essais += 1

        # si la guess est égale a value
        elif guess == value:
            # augmente le nombre d'essai de 1 et félicite le joueur en le montrant ses nb_essais
            nb_essais += 1
            print(f"Bravo! Bonne réponse\nVous avez réussi en : {nb_essais} essai(s).")
            # demande au jour s'il veut recommencer une partie
            recommencer = (input("Voulez-vous faire une autre partie (o/n)? _\n"))

            # si oui, relance le jeux
            if recommencer == "o":
                devinette()
            # si non, au revoir
            elif recommencer == "n":
                print("Merci et au revoir...")
            # error si le joueur ne répond pas correctement a la question
            else:
                print("error")
            # casse la boucle, ce qui arrête le programme
            break


# Lance le jeux quand le programme est lancé
devinette()
