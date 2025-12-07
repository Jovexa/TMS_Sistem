# FAJL: day14_app.py
# Glavni interfejs (koristi while petlju iz Dana 8)

import tms_lib # Uvozimo našu radionicu (Dan 12)

def main():
    # Naša baza podataka u memoriji (Dan 5)
    my_fleet = []
    
    # Dodajemo par kamiona da ne bude prazno na početku
    my_fleet.append(tms_lib.create_truck("T-101", "Volvo 780"))
    my_fleet.append(tms_lib.create_truck("T-102", "Mack Anthem", "Maintenance"))
    my_fleet.append(tms_lib.create_truck("T-103", "Peterbilt", "Available"))

    print("--- TMS SYSTEM v0.2 (WEEK 2 FINAL) ---")

    # GLAVNA PETLJA (Dan 8)
    while True:
        print("\nMENI:")
        print("1. Prikaži sve kamione")
        print("2. Prikaži samo slobodne (Available)")
        print("3. Dodaj zaradu kamionu")
        print("4. Finansijski Izveštaj (Total)")
        print("5. Izlaz")
        
        choice = input("Izbor > ")

        if choice == "1":
            tms_lib.show_fleet_report(my_fleet)
        
        elif choice == "2":
            # Koristimo pametno filtriranje iz biblioteke
            free_trucks = tms_lib.get_active_trucks(my_fleet)
            print("\n--- SLOBODNI KAMIONI ---")
            tms_lib.show_fleet_report(free_trucks)

        elif choice == "3":
            t_id = input("Unesi ID kamiona: ")
            amount = float(input("Unesi iznos ($): "))
            
            # Tražimo kamion (Mala petlja)
            found = False
            for truck in my_fleet:
                if truck["id"] == t_id:
                    tms_lib.add_revenue(truck, amount)
                    print(f"✅ Dodato ${amount} na kamion {t_id}")
                    found = True
                    break # Prekidamo petlju jer smo ga našli
            
            if not found:
                print("❌ Kamion nije pronađen!")

        elif choice == "4":
            total = tms_lib.calculate_total_revenue(my_fleet)
            print(f"\n💰 UKUPAN PROMET FIRME: ${total:.2f}")

        elif choice == "5":
            print("Gašenje sistema...")
            break
        
        else:
            print("Nepoznata opcija.")

# Pokretanje
if __name__ == "__main__":
    main()