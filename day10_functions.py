#Functions PArt 1 - Trucking Utility Library
#Ucimo kako da napravimo svoje komande (funkcije) koje obavljaju odredjene zadatke def

print("---TMS KALKUALTORI FUNKCIJE v1.0 ---")

# --- Definisanje alata funkcija ---
#Ovde samo pravimo funkcije, ne pozivamo ih jos uvek

def calcualte_revenue(miles, rate):
    """Izracunava prihod na osnovu milja i cene po milji.
    Ulaz: milje, cene po milji.
    Izlaz: prihod (float) """

    revenue = miles * rate
    return revenue  #Vraca izracunati prihod

def calculate_fuel_cost(miles, mpg, fuel_price):
    """Izracunava troskove goriva na osnovu milja, mpg i cene goriva.
    Ulaz: milje, mpg, cena goriva po galonu.  
    Formula: (Milje / MPG) * Cena Dizela
    Izlaz: troskovi goriva (float) """

    gallons_used = miles / mpg
    cost = gallons_used * fuel_price
    return cost  #Vraca izracunate troskove goriva

def calculate_profit(revenue, expenses):
    """Izracunava profit na osnovu prihoda i troskova.
    Ulaz: prihod, troskovi.
    Izlaz: profit (float) """

    profit = revenue - expenses
    return profit  #Vraca izracunati profit

# --- Glavni program ---
#Ovde pozivamo funkcije i koristimo ih kao dispecer koji kontrolise kalkulatore

print("\n...Racunam turu Chicago to Miami...")

#1.pozivanje funkcije za prihod
distanca = 1300  #milje
cena_ture = 2.50 #cena po milji $
zarada = calcualte_revenue(distanca, cena_ture)
print(f"Prihod od ture: ${zarada:.2f}")

#2. Pozivanje funkcije za troskove goriva
moj_mpg = 6.5    #kamion mpg
cena_dizela = 3.85 #cena goriva po galonu $
trosak_goriva = calculate_fuel_cost(distanca, moj_mpg, cena_dizela)
print(f"Troskovi goriva za turu: ${trosak_goriva:.2f}")

#3. Pozivamo alat za profit
#Dodatni troskovi (putarine, hrana, smestaj)

driver_pay = 600
tolls = 150
ukupni_troskovi = trosak_goriva + driver_pay + tolls

cist_profit = calculate_profit(zarada, ukupni_troskovi)

print("-" * 30)
print(f"💵 Prihod:          ${zarada:.2f}")          # (Opciono: Lepo je videti i ovo opet)
print(f"💸 Ukupni Troškovi: ${ukupni_troskovi:.2f}") # 🆕 <--- DODAJ OVO!
print("-" * 30)
print(f"💰 ČIST PROFIT TURE: ${cist_profit:.2f}")
print("-" * 30)


    