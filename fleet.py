#Fleet Tracker Module (Uvod u Liste i Petlje)

print('---TMS FLEET MANAGEMET SYSTEM---')
#1. Kreiranje liste vozila u floti (POcinjemo sa 2 kamiona na parkingu)
fleet = ["Volvo 780", "Freightliner Cascadia"]

print(f"Pocetno stanje flote: {fleet}")

#2. Dodavanje novog vozila u flotu (Novi kamion je stigao)
print("\nDodavanje novog vozila u flotu...")
fleet.append("Kenworth T680")  # Dodajemo novi kamion na kraj liste
fleet.append("Peterbilt 579")
fleet.append("Mack Anthem")


#3. Prikazivanje (foor loop) svih vozila u floti
#Ovo je "For Loop" petlja koja prolazi kroz svaki element u listi
print("\n---Trenutna flota vozila(POPIS)--- ")
for truck in fleet:
    #Ova linije stampa svaki kamion u floti
    print(f"Kamioun u floti: {truck}")
    
    #4. Brisanje vozila iz flote (Kamion je prodat)
    print('\n... Mack Anthem je prodat ...')
    kamion_za_prodaju = "Mack Anthem"
    if kamion_za_prodaju in fleet:
        fleet.remove(kamion_za_prodaju)
        print(f"✅ Uspešno obrisan: {kamion_za_prodaju}")
    else:
        print(f"⚠️ GREŠKA: Kamion '{kamion_za_prodaju}' nije nađen na parkingu!")

#5. Indeksiranje ( Pronalazenje pozicije kamiona u listi)
# U programiranje indeksi pocinju od 0
first_truck = fleet[0]  # Prvi kamion u floti
last_truck = fleet[-1] # Poslednji kamion u floti koristeci negativni indeks

print(f"\nPrvi kamion u floti je: {first_truck}")
print(f"Poslednji kamion u floti je: {last_truck}")

#6. Ukupno vozila u floti
total_trucks = len(fleet)  # len() funkcija vraca broj elemenata u listi
print("_" * 30 )
print(f"Ukupno vozila u floti: {total_trucks}")
print(f"Lista flote: {fleet}")
print("_" * 30 )


