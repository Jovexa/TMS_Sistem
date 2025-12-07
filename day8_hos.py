#HOS Hours of Service Rules
# Ucimo: while loops, break, continue

print("---ELD SISTEM AKTIVAN ---   ")
print("Maksimalno vreme vozenjea: 11 sati")

#1. Pocetno stanje
total_driving_hours = 0.0
limit = 11.0

#2.While loop - simulacija voznje
#Dokle god je ukupno vreme voznje manje od limita radi sledece:
#Ali mi cemo koristiti while True da bismo rucno kontrolisali kraj petlje

while True:
    #Prikaz statusa
    print(f"\nTrenutno ukupno vreme voznje: {total_driving_hours} sati")
    #3. Unos od korisnika
    unos = input("Unesi sat voznje (ili 'kraj' za izlaz): ")

    #4. Provera za izlaz (break)
    if unos.lower() == 'kraj':
        print("Sistem iskljucen. Doviđenja!")
        break  #prekida while petlju

    #5. Konverzija i Validacija unosa
    #Moramo proveriti da li je unos validan broj, ako nije preskacemo krug.
    if not unos.replace('.','',1).isdigit(): #provera da li je broj (dozvoljen decimalni broj)
        print("GRESKA. Molimo unesite broj sati ili 'kraj'.")
        continue  #preskace ostatak koda i vraca se na pocetak petlje

    hours = float(unos)

    #Provera da li je uneo negativan broj
    if hours < 0:
        print("GRESKA. Vreme voznje ne moze biti negativno.")
        continue

    #6. Glavna logika - Dodavanje sati voznje
    #Proveravamo da li dodavanje ovih sati prelazi limit
    temp_total = total_driving_hours + hours

    if temp_total > limit:
        print(f"VIOLATION ALERT! Hteli ste da vozite{hours}h.")  #Dodavanje ovog vremena prelazi limit od {limit}h.")
        print(f"To bi dovelo do ukupnog vremena voznje od {temp_total}h, sto prelazi dozvoljeni limit od {limit}h.")
        print("Voznja je blokirana da bi se izbegla povreda HOS pravila. Morate odmoriti pre nastavka voznje.")
        #Ovde mozemo staviti break ako zelimo da izadjemo iz petlje
        #ili samo pustiti da proba ponovo manji unos
        break  #Izlazimo iz petlje nakon povrede

    #Ako je sve OK, dodajemo pravo vreme voznje
    total_driving_hours += hours
    remaining = limit - total_driving_hours

    print(f"Unos prihvacen. Preostalo vreme voznje danas: {remaining:.2f} sati.")

    #Dodatna provera ako je tacno na nuli
    if remaining == 0:
        print("⚠️ VREME ISTEKLO! Parkiraj kamion.")
        break

print("--- KRAJ SMENE ---")
