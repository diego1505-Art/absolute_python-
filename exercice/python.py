questions = [
    ("quelle est la capitale de la france ?", "paris"),
    ("combien font 3 x 7 ?", "21"),
    ("quelle est la couleur du ciel ?", "bleu"),
    ("combien de jours dans une semaine ?", "7"),
    ("quelle est la capitale de l'espagne ?", "madrid"),
]

score = 0
numero = 0

print("=== BIENVENUE DANS LE QUIZ ===")
print("tape 'quitter' a tout moment pour arreter\n")

while numero < len(questions):
    question, bonne_reponse = questions[numero]

    while True:
        reponse = input(f"question {numero + 1} : {question} ").lower()

        if reponse == "quitter":
            print("\ntu as quitte le jeu !")
            print(f"ton score final est : {score}/{numero}")
            break

        if reponse == "":
            print("tu ne peux pas laisser vide, reessaie !")
            continue

        if reponse == bonne_reponse:
            print("bonne reponse !\n")
            score += 1
            break
        else:
            print("mauvaise reponse, reessaie !\n")

    if reponse == "quitter":
        break

    numero += 1

else:
    print("=== FIN DU QUIZ ===")
    print(f"ton score final est : {score}/{len(questions)}")

    if score == len(questions):
        print("parfait, tu as tout bon !")
    elif score >= 3:
        print("bien joue !")
    else:
        print("tu peux mieux faire, reessaie !")