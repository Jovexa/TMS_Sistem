# DAY 7: Mini TMS Command Line Interface v0.1

# Lista gde čuvamo kamione. Biće lista rečnika (dictionaries) - mali sneak peek za Week 3
# Svaki kamion je rečnik sa ID-jem i vozačem.
fleet = []
total_revenue = 0.0

# Glavna petlja programa - vrti se beskonačno dok ne izaberemo "Izlaz"
while True:
    # --- MENI ---
    print("\n--- Mini TMS Glavni Meni ---")
    print("1. Dodaj novi kamion")
    print("2. Pokaži celu flotu")
    print("3. Unesi novu turu")
    print("4. Pokaži ukupan promet")
    print("5. Izlaz")
    
    # Pitamo korisnika šta želi da radi
    choice = input("Izaberite opciju (1-5): ")
    
    # --- LOGIKA MENIJA (IF/ELIF/ELSE) ---
    
    if choice == '1':
        # DODAJ KAMION
        print("\n-- Dodavanje Novog Kamiona --")
        truck_id = input("Unesi ID kamiona: ")
        driver_name = input("Unesi ime vozača: ")
        
        # Kreiramo rečnik za kamion
        truck = {"id": truck_id, "driver": driver_name}
        fleet.append(truck)
        print(f"✅ Kamion {truck_id} sa vozačem {driver_name} je dodat.")
        
    elif choice == '2':
        # POKAŽI FLOTU
        print("\n-- Lista Svih Kamiona --")
        if not fleet: # Ako je lista prazna
            print("Flota je trenutno prazna.")
        else:
            for truck in fleet:
                print(f"ID: {truck['id']}, Vozač: {truck['driver']}")
                
    elif choice == '3':
        # UNESI TURU
        print("\n-- Unos Nove Ture --")
        miles = float(input("Unesi broj milja: "))
        rate = float(input("Unesi cenu po milji ($): "))
        
        revenue = miles * rate
        total_revenue += revenue # Dodajemo na ukupan promet
        print(f"💰 Tura uspešno uneta. Prihod: ${revenue:.2f}")

    elif choice == '4':
        # POKAŽI PROMET
        print(f"\n-- Ukupan Promet --")
        print(f"Ukupan prihod od svih tura: ${total_revenue:.2f}")

    elif choice == '5':
        # IZLAZ IZ PROGRAMA
        print("Doviđenja!")
        break # Ova komanda prekida 'while True' petlju
        
    else:
        # POGREŠAN UNOS
        print("❌ Nepoznata opcija. Molimo izaberite broj od 1 do 5.")