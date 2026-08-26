# ============================================================
#  L'enfer des if enchaînés — vs — try/except
# ============================================================

# Teste ces valeurs une par une pour voir ce qui se passe :
# "5", "0", "abc", "1.5", "1e10", " 3 ", "", "-4"

valeur = input("Entre un nombre pour diviser 10 : ")


# ------------------------------------------------------------
# VERSION if/else : on essaie de tout anticiper...
# ------------------------------------------------------------

print("\n--- AVEC if/else ---")

if valeur == "":
    print("Erreur : t'as rien tapé !")
elif valeur.strip() != valeur:
    print("Erreur : y'a des espaces au début ou à la fin !")
elif valeur == "0":
    print("Erreur : division par zéro !")
elif "e" in valeur or "E" in valeur:
    print("Erreur : notation scientifique non supportée !")
elif "." in valeur:
    print("Erreur : les décimaux ne sont pas supportés !")
elif not valeur.lstrip("-").isdigit():
    print("Erreur : c'est pas un nombre !")
elif int(valeur) < 0:
    print("Erreur : les négatifs ne sont pas supportés !")
else:
    print("Résultat : 10 / " + valeur + " = " + str(10 / int(valeur)))

# Et pourtant... "1.5" passe le filtre "." mais float("1.5") marche très bien.
# On a INTERDIT des cas valides à force de vouloir tout contrôler.
# Et on a encore probablement oublié des cas !


# ------------------------------------------------------------
# VERSION try/except : on tente, Python gère les vrais problèmes
# ------------------------------------------------------------

print("\n--- AVEC try/except ---")

try:
    resultat = 10 / float(valeur)
    print("Résultat : 10 / " + valeur + " = " + str(resultat))
except ZeroDivisionError:
    print("Erreur : division par zéro !")
except ValueError:
    print("Erreur : c'est pas un nombre valide !")

# 5 lignes. Gère tous les cas. Accepte "1.5", "1e10", " 3 ", "-4".
# Python sait mieux que nous ce que float() accepte ou non.
