vards = input("Tavs vārds").capitalize()
uzvards = input("Tavs uzvārds").capitalize()
print(f"Sveicināts/a {vards} {uzvards} !")

def main():
    eiro = eiro_uz_float(input("Cik maksaja pirkums? "))

    procenti = procenti_uz_float(input("Kāda ir procentuala dala atlaidei? "))
    atlaide = eiro * procenti
    print(f"Klienta dati : {vards} {uzvards}")
    print(f"Atlaide : {procenti * 100} %")
    print(f"Pirkuma summa pirms atlaides {eiro} €")
    print(f"Pirkuma summas atlaide ir {atlaide:.2f} €")

def eiro_uz_float(e):
    e = e.replace('€', '')
    return float(e)

def procenti_uz_float(p):
    p = p.replace('%', '')
    return float(p) / 100

main()

