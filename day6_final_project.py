# Day 6 Comprehensive Truck Calculator
# Cilj: Izracunati profitabilnost ture koristeci sve naucene koncepte

print("---TMS PROFIT ANALYZER TOOL---")

#1. priprema praznih lista (Parking mesta)
#Ovde cemo cuvati podatke da bismo ih kasnije analizirali
imena_kamiona = []
profiti_kamiona = []

#2. Unos podataka (Petlja za unos vise kamiona)
# Zelimo podatke za 3 kamiona, Koristimo range(3) za 3 ponavljanja
for i in range(3):
    print(f"\n---Unos podataka za kamion #{i+1}---")

    #Input podataka
    ime = input('Unesi ID kamiona (npr. Volvo 780): ')
    prihod = float(input(" Unesiukupan PRIHOD ($): "))
    trosak = float(input(" Unesi ukupne TROSKOVE ($): "))

    #logika: Izracunavanje profita
    profit = prihod - trosak

    # Ubacivanje u liste (Spremanje podataka za kasniju analizu)
    imena_kamiona.append(ime)  # Dodajemo ime kamiona u listu
    profiti_kamiona.append(profit)  # Dodajemo profit u listu

    print(f"Profit za kamion '{ime}': ${profit:.2f}") # Prikaz profita sa 2 decimale

#3. Analiza podataka nakon unosa svih kamiona
print('\n' + "=" * 30) # Linija za razdvajanje
print("IZVESTAJ FLOTE - PROFITABILNOST KAMIONA")
print("=" * 30)   # Linija za razdvajanje

#a) Ukupan profit svih kamiona
total_profit = 0
for p in profiti_kamiona:
    total_profit += p

#b)Prosecan profit po kamionu
# #Pazi: Ne smemo deliti sa nulom, ali ovde uvek imamo 3 kamiona.
broj_kamiona = len(profiti_kamiona)
average_profit = total_profit / broj_kamiona


# #c) Najprofitabilniji kamion (Logika trazenja maksimuma)
# Ovo je klasican algoritam: "King of the Hill" za pronalazenje maksimuma
# 
max_profit = -100000  # Postavljamo na vrlo nisku vrednost
najbolji_kamion = ""

# Prolazimo kroz sve profite da nadjemo najveci
# enumerate() nam daje i indeks(0,1,2) i vrednost iz liste profiti_kamiona
for index, profit in enumerate(profiti_kamiona):
    if profit > max_profit:
        max_profit = profit    # Azuriramo maksimum
        najbolji_kamion = imena_kamiona[index]   # Cuvamo ime kamiona sa najveciim profitom

#4. Finalni ispis rezultata
print(f"UKUPNP KAMIONA: {broj_kamiona}")
print(f"UKUPAN PROFIT SVIH KAMIONA: ${total_profit:.2f}")  # Prikaz sa 2 decimale
print(f"PROSEČAN PROFIT PO KAMIONU: ${average_profit:.2f}")
print("-" * 30)
print(f"NAJPROFITABILNIJI KAMION: {najbolji_kamion} sa profitom od ${max_profit:.2f}")
print("=" * 30)

# Kraj programa

   

    
    