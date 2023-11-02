def sveiciens():
    vards = input("Kā tevi sauc?")
    print(f"Labdien, {vards}!")
    

def pirkums():
    cena1 = int(input("Cik maksā 1. prece?"))
    cena2 = int(input("Cik maksā 2. prece?"))
    summa = cena1 + cena2
    print(summa)
    return summa


def atlaides_aprekins():
    atlaide = input("Cik % ir atlaide?").replace(",",".").strip(" %")
    atlaide_decimal = atlaides_parveidosana(atlaide)
    summa = pirkums()
    jamaksa = summa - summa * atlaide_decimal
    print(f"Summa pēc atlaides piemērošanas {jamaksa}")
    

def atlaides_parveidosana(atlaide):
    atlaide_decimal = float(atlaide)/100
    return atlaide_decimal

# sveiciens()
#pirkums()
atlaides_aprekins()
