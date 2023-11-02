# Par darba veikšanu patstāvīgi 2 punkti. T.i., sēžot atsevišķi, nekonsultējoties ar apkārtējiem.
# Saņemt 10 var vienīgi izpildot šo nosacījumu.


# 1. Izveido teksta mainīgo ar šī mēneša nosaukumu (1 p.)
menesis = "novembris"
print(menesis)

# 2. Doti divi skaitliski mainīgie.
# Ar print parādi pirmā mainīgā dalījumu ar otro  (1 p.)
ska1 = 10
ska2 = 11

print(ska1/ska2)

# 3. Izmantojot print ar f-string, kā arī dotos mainīgos, izveido nepieciešamo izteiksmi un izvadi ekrānā teikumu,
# kurš parāda cik dienas atlikušas līdz gada beigām. (2 p.)
novembris = 30
decembris = 31
gads = 2023

atlikušas_dienas = (novembris+decembris)
print(f"Līdz 2023. gada beigām atlikušas {atlikušas_dienas} dienas!")

# 4. Dotajā koda rindā ir kļūda, izlabo! (1 p.)
gads = int(input("Uzraksti, kāds tagad gads!"))


# 5. Maini sk1, sk2 un sk3 vērtības, lai dotā rinda ar print parādītu False (2 p.)
sk1 = 4
sk2 = 2
sk3 = 3
print(sk1 == sk2 or sk1 < sk3)


# 6. Izmanto dotos mainīgos un izveido izteiksmi, kura aprēķina visu preču vērtību centos. 
# Atbildei jābūt jaunam mainīgajam precu_summa (1 p.)
precu_skaits = 2
preces_cena_eur = 3

print(preces_cena_eur*precu_skaits*2)


# 7. Uzstādi komentāra zīmi visu iepriekšēju koda rindu priekšā. (1 p.)



# 8. Izveido funkciju kapinajums ar vienu parametru, kuram jābūt veselam skaitlim.
# Funkcijai to jāatgriež kāpinātu tādā pašā pakāpē, kā šis skaitlis. (2 p.)

a=int(input("Ievadiet skaitli"))
print(a**a)


# 9. Izveido funkciju divi_skaitli ar diviem skaitliskiem parametriem.
# Ja ja pirmais skaitlis lielāks par otro, tad programma parāda abu skaitļu starpību,
# ja otrais lielāks par pirmo – abu skaitļu summu,
# ja abi vienādi – parāda dubultotu summu. (3 p.)

a=4
b=3
if a>b :
    print(a-b)
elif a<b :
    print (a+b)
else :
    a==b
    c=a+b
    print(c*2)

# 10. Izveido funkciju jauna_parole bez parametriem. 
# Funkcijā pieprasa ievadīt divus vārdu vai simbolu virknes.
# Ja tie ievadīti vienādi, tad paziņo "Parole izveidota veiksmīgi." 
# Ja nav vienādi, atkārtoti pieprasa divus vārdus.
# Papildus prasība – ja jebkurš no ievadītajiem vārdiem ir STOP, 
# programma darbu beidz un paziņo "Paroles maiņa atlikta." (4 p.)

def jauna_parole():
    a=input("Ievadi vārdu vai skaitļu virkni:")
    b=input("Ievadiet šo virkni atkārtoti:")
    if a==b:
        print("parole izveidota veiksmīgi")

    elif a!=b:
        jauna_parole()

    else:
        a or b == STOP
        print ("Paroles maiņa atlikta.")

jauna_parole()
# 11. paskaidro šos operatorus (0.5 p par katru)
# //  kvadratsakne
# ==  salidzinat mainigos
# =   pieskirt mainigo
# and  un

 

# 12. Aizpildi teksta mainīgos labiSapratu un velJapamacas un izlabo skaitlisko mainīgo atzime,
# lai zemāk dotā print rinda parādītu Tavu pašvērtējumu par darbu un paredzamo atzīmi. 
labiSapratu = "funkciju veidošana"
velJapamacas = "mainīgo sastādīšana"
atzime = 8

print(f"Manuprāt vislabāk sapratu un izdevās {labiSapratu},\nbet vēl jāuzlabo {velJapamacas}.\nDomāju, ka saņemšu {atzime}.")

# Paldies par darbu!
