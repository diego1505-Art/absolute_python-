import random
import string

# ============================================
# CONFIG
# ============================================

OUTPUT_FILE = r"C:\Users\diego\Documents\python lol\milliard_mots.txt"

TOTAL_WORDS = 1_000_000_000
BATCH_SIZE = 100_000

# ============================================
# CARACTÈRES POSSIBLES
# ============================================

CHARS = (
    string.ascii_letters +
    string.digits +
    "!@#$%^&*()_+-=[]{}|;:,.<>?/"
)

# ============================================
# GÉNÉRATION MOT ALÉATOIRE
# ============================================

def random_word():

    length = random.randint(3, 20)

    return ''.join(
        random.choice(CHARS)
        for _ in range(length)
    )

# ============================================
# ÉCRITURE FICHIER
# ============================================

written = 0

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:

    while written < TOTAL_WORDS:

        words = []

        for _ in range(BATCH_SIZE):

            if written >= TOTAL_WORDS:
                break

            words.append(random_word())
            written += 1

        f.write(' '.join(words) + ' ')

        print(f"{written:,} mots générés")

print("TERMINÉ")
print("Fichier créé :", OUTPUT_FILE)