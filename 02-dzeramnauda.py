def main():
    eiro = eiro_uz_float(input("Cik maksaja maltite?"))
    procenti = procenti_uz_float(input("Kādu procentualo dalu velaties atstat ka dzeramnaudu?"))
    dzeramnauda = eiro * procenti
    print(f"Atstājiet {dzeramnauda:.2f} €")

     
def eiro_uz_float(e):
    e = e.replace('€', '')
    return float (e)

def procenti_uz_float(p):
    p = p.replace('%', '')
    return float(p) / 100

main()
                                 
