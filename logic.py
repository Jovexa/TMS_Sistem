#Load & Route Analyzer
#cilj: Proveriti tipove podataka(int, float, str) i logiku (if-else) za analizu tereta i rute
print("--- TMS LOAD & ROUTE ANALYZER ---")

#Tipovi podataka
#input() funkcija uvek vraca string. Moramo konvertovati u int ili float za racunanje
wight_str = input("Unesi tezinu tereta (lbs): ")
miles_str = input("Unesi duzinu rute (miles): ")

#Konverzija ovo je kljucni korak
weight = float(wight_str)  # Pretvaramo u float za preciznost moze biti 450.5 lbs
miles = int(miles_str)      # Pretvaramo u int jer su milje obicno celobrojne

print(f"\nAnaliza tereta od {weight} lbs na distanci od {miles} milja.")
print ("-" * 30)


#Logika i komparacije
# Provera tezine tereta( Load Weight Validation)

limit = 80000  # Maksimalna tezina tereta u lbs
if weight > limit:
    print(f"❌ OVERWEIGHT! Prešli ste limit za {weight - limit} lbs.")
    status = "ILLEGAL"
else:
    print("✅ TEŽINA OK. Može da vozi.")
    status = "LEGAL"

    #Klasifikacija Rute (Route Classification)
    category = ""
    if miles<250:
        category = "SHORT HAUL"
    elif miles>=250 and miles<=500:   #Koristimo elif i and za vise uslova
        category = "MEDIUM HAUL"
    else:
        category = "LONG HAUL"
    print(f"Tip rute: {category}")

    #Napredna logika(Slozena odluka)

    #primer: Ako je Long haul, tezina mora biti maksimalno 70000 lbs zbog goriva - Izmisljena restrikcija
    if category == "Long Haul 🌎" and weight > 75000:
        print("⚠️ UPOZORENJE: Teška tura za Long Haul! Proveri potrošnju goriva.")
    print("-" * 30)
#Kraj analize
