# DAY 15: Nested Dictionaries (Rečnik u Rečniku)
# Ovo je najbrži način da čuvaš podatke u Pythonu.

print("--- TMS FLEET DATABASE (DICT VERSION) ---")

# 1. KREIRANJE FLOTE (Rečnik rečnika)
# KLJUČ (Key) = ID Kamiona (Jedinstven)
# VREDNOST (Value) = Ceo profil kamiona (Drugi rečnik)

fleet = {
    "T-101": {
        "driver": "Marko Markovic",
        "status": "Available",
        "miles": 120000
    },
    "T-102": {
        "driver": "Jovan Jovanovic",
        "status": "Maintenance",
        "miles": 155000
    },
    "T-103": {
        "driver": "Ivan Ivic",
        "status": "On Load",
        "miles": 89000
    }
}

# 2. PRISTUP PODACIMA (Brza pretraga)
# Hoćemo da nađemo ko vozi T-102.
# Ne moramo da vrtimo petlju! Samo ga "pozovemo" po imenu.

search_id = "T-102"

if search_id in fleet:
    # Ovako ulazimo duboko: fleet["ID"]["driver"]
    vozac = fleet[search_id]["driver"]
    stanje = fleet[search_id]["status"]
    print(f"🔍 Pronađen kamion {search_id}: Vozi ga {vozac}, status je {stanje}.")
else:
    print("❌ Kamion nije pronađen.")

# 3. DODAVANJE NOVOG KAMIONA U FLOTU
print("\n... Kupujemo novi kamion T-104 ...")
fleet["T-104"] = {
    "driver": "Novi Vozac",
    "status": "Available",
    "miles": 0
}

# 4. IZVEŠTAJ (Petlja kroz ugnježdene rečnike)
print("\n--- IZVEŠTAJ CELA FLOTA ---")

# k = ID kamiona (npr. "T-101")
# v = Rečnik sa podacima ({"driver": "Marko"...})
for truck_id, data in fleet.items():
    print(f"ID: {truck_id} | Vozač: {data['driver']} | Status: {data['status']}")

print("-" * 30)