frase_teamo = ["Te amo", "Te amo, amu", "Te amo, muchita", "Te amo, Chuek"]
frase_teextraño = ["Te extraño", "Te extraño, Chuek", "Te extraño, amor"]

norma = input("Escribe algo, Chuek: ")

if norma in frase_teamo:
    print("Yo también te amo")
    print("Y mucho")
elif norma in frase_teextraño:
    print("Yo también te extraño")
elif norma == "algo":
    print("'Algo' no cuenta")
else:
    print("Yo te amo aunque no escribas que me amas o extrañas")
