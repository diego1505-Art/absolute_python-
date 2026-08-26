def cesar_encrypt(texte, decalage):
    result = []

    for lettre in texte:
        if 'a' <= lettre <= 'z':
            base = ord('a')
            code = (ord(lettre) - base + decalage) % 26 + base
            result.append(chr(code))

        elif 'A' <= lettre <= 'Z':
            base = ord('A')
            code = (ord(lettre) - base + decalage) % 26 + base
            result.append(chr(code))

        else:
            result.append(lettre)

    return ''.join(result)


while True:
    message = input("Message à chiffrer : ")
    decalage = int(input("Décalage à appliquer : "))
    print("Message chiffré :", cesar_encrypt(message, decalage))

    reponse = input("Voulez-vous quitter ? (yes/no) ")

    if reponse == "yes":
        break
    elif reponse == "no":
        continue