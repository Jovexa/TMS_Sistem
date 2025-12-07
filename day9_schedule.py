# DAY 9: Weekly Schedule Generator
# Učimo: Nested Loops (Petlja u petlji)

print("--- TMS NEDELJNI RASPORED v1.0 ---")

# 1. DEFINISANJE PODATAKA (Liste)
# Ovo su naše "ose" tabele (X i Y)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
trucks = ["Volvo 780", "Mack Anthem", "Peterbilt 579"]

# 2. NESTED LOOPS (Glavni motor)

# SPOLJNA PETLJA: Kontroliše DANE (Ide sporo)
for day in days:
    print(f"\n📅 DAN: {day.upper()}")
    print("-" * 40)
    
    # UNUTRAŠNJA PETLJA: Kontroliše KAMIONE (Ide brzo)
    # Ova petlja se izvrši KOMPLETNO za svaki pojedinačni dan!
    for truck in trucks:
        
        # 3. LOGIKA STATUSA (Odlučivanje)
        status = "🟢 DISPATCHED" # Standardno stanje (Radni dan)
        
        # Provera za Vikend (Subota i Nedelja)
        if day == "Saturday" or day == "Sunday":
            # Vikendom vozi samo Volvo, ostali odmaraju
            if truck == "Volvo 780":
                status = "🟡 DEŽURSTVO (Weekend Shift)"
            else:
                status = "🔴 PARKIRAN (Off Duty)"
        
        # Specifičan izuzetak: Peterbilt ide na servis u Sredu
        if day == "Wednesday" and truck == "Peterbilt 579":
            status = "🔧 SERVIS (Maintenance)"

        # 4. PRIKAZ (Output)
        # \t je "Tab" (razmak) da lepše izgleda
        print(f"   🚛 {truck}: \t{status}")

print("\n" + "="*40)
print("Raspored uspešno generisan.")