# FAJL: day12_main.py
# OVO JE GLAVNI ULAZ U APLIKACIJU

# 1. UVOZIMO NAŠE NOVE MODULE
# Pazi: Imena fajlova moraju biti tačna (bez .py na kraju ovde)
import truck_utils
import load_utils

# Alternativni način (češće se koristi):
# from truck_utils import create_truck, get_truck_info

def main():
    print("--- TMS MODULAR SYSTEM START ---\n")

    # --- KORAK A: Rad sa kamionima (Zovemo radionicu) ---
    print("1. Kreiranje kamiona...")
    my_truck = truck_utils.create_truck("VOLVO-780")
    print(truck_utils.get_truck_info(my_truck))

    # --- KORAK B: Rad sa turom (Zovemo računovodstvo) ---
    print("\n2. Obrada ture...")
    load_miles = 600
    load_rate = 2.50
    load_weight = 42000

    # Provera težine (iz load_utils)
    is_legal, message = load_utils.verify_weight(load_weight)
    print(f"Status Vage: {message}")

    if is_legal:
        # Računanje para (iz load_utils)
        revenue = load_utils.calculate_revenue(load_miles, load_rate)
        print(load_utils.format_rate_con("L-1001", revenue))
        
        # Ažuriranje kamiona (iz truck_utils)
        truck_utils.update_status(my_truck, "On Load")
        print(f"\nNOVI STATUS: {truck_utils.get_truck_info(my_truck)}")
    else:
        print("Tura odbijena zbog težine.")

# --- POKRETANJE SISTEMA ---
if __name__ == "__main__":
    main()