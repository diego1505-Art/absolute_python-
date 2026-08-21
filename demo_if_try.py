# ============================================================
#  Démonstration : if/else  vs  try/except
# ============================================================


# ------------------------------------------------------------
# SCÉNARIO 1 — Division
# On veut diviser 10 par un nombre entré par l'utilisateur
# ------------------------------------------------------------

valeur = input("Entre un nombre pour diviser 10 : ")

# Avec if/else : on VÉRIFIE avant d'agir
if valeur == "0":
    print("[if/else]   Impossible, division par zéro !")
else:
    print(f"[if/else]   10 / {valeur} = {10 / float(valeur)}")
# Problème : si l'utilisateur tape "abc", float("abc") va planter !
# Le if/else ne protège pas contre tous les cas.

print()

# Avec try/except : on TENTE et on gère les erreurs
try:
    resultat = 10 / float(valeur)
    print(f"[try/except] 10 / {valeur} = {resultat}")
except ZeroDivisionError:
    print("[try/except] Impossible, division par zéro !")
except ValueError:
    print("[try/except] Ce n'est pas un nombre valide !")
# Ici on gère TOUS les cas d'erreur possibles, même les imprévus.


print()
print("=" * 50)
print()


# ------------------------------------------------------------
# SCÉNARIO 2 — Accès à un fichier
# Lire un fichier qui n'existe peut-être pas
# ------------------------------------------------------------

nom_fichier = "mon_fichier.txt"

# Avec if/else : on vérifie si le fichier existe avant
import os

if os.path.exists(nom_fichier):
    with open(nom_fichier) as f:
        print(f"[if/else]   Contenu : {f.read()}")
else:
    print("[if/else]   Le fichier n'existe pas.")
# Problème : entre le if et le open(), quelqu'un pourrait
# supprimer le fichier (rare, mais possible).

print()

# Avec try/except : on tente directement, plus sûr et plus simple
try:
    with open(nom_fichier) as f:
        print(f"[try/except] Contenu : {f.read()}")
except FileNotFoundError:
    print("[try/except] Le fichier n'existe pas.")
except PermissionError:
    print("[try/except] Pas le droit de lire ce fichier.")


print()
print("=" * 50)
print()


# ------------------------------------------------------------
# SCÉNARIO 3 — Logique métier normale → if/else est mieux
# Vérifier si un utilisateur est majeur
# ------------------------------------------------------------

age = 20  # valeur fixe pour l'exemple

# Ici if/else est PARFAIT : c'est une condition logique simple,
# pas une erreur. On n'attend pas d'exception.
if age >= 18:
    print(f"[if/else]   {age} ans → Majeur ✓")
else:
    print(f"[if/else]   {age} ans → Mineur ✗")

# try/except ici n'aurait aucun sens, il n'y a rien qui peut "planter".


# ------------------------------------------------------------
# RÉSUMÉ
# ------------------------------------------------------------
print()
print("RÉSUMÉ")
print("  if/else   → condition LOGIQUE et PRÉVISIBLE (majeur/mineur, vide/plein...)")
print("  try/except → erreur POSSIBLE et IMPRÉVISIBLE (fichier, réseau, conversion...)")
