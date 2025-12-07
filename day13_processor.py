#List Comprehensions Pythonic Code
#Cilj: Obrada podataka u jednoj liniji koda

print("---FLEET DATA PROCESSOR v1.0---")
#podaci Raw data
#Lista ID-ijeva kamiona u floti ( neki su mala slova, neki velika)

raw_ids = ["t-001", "T-002", "t-003", "T-004"]

#Lista tura sa brojem milja
miles_list = [450, 1200, 300, 850, 2000]

#lista kamiona sa statusom

trucks = [
    {"id": "T-101", "status": "Active"},
    {"id": "T-102", "status": "Maintenance"},
    {"id": "T-103", "status": "Active"},
    {"id": "T-104", "status": "Sold"},
]

print(f"Original IDs: {raw_ids}")

#----------------------
#Zadatak 1: Svi ID-jevi u velikim slovima Basic Comprehension
#----------------------

# ❌ STARI NAČIN (3 linije)
clean_ids_old = []
for tid in raw_ids:
    clean_ids_old.append(tid.upper())

   # ✅ NOVI NAČIN (1 linija)
# [AKCIJA for PREDMET in LISTA]
clean_ids = [tid.upper() for tid in raw_ids]
print(f"Čisti ID-jevi: {clean_ids}")

# ---------------------------------------------------------
# ZADATAK 2: Računanje prihoda (MATH COMPREHENSION)
# ---------------------------------------------------------
rate = 2.50 # Cena po milji

# Želimo listu zarada za svaku turu
# ✅ NOVI NAČIN:
revenues = [miles * rate for miles in miles_list]
print(f"Prihodi po turama: {revenues}")
# Ukupan prihod
print(f"Ukupan prihod: ${sum(revenues):.2f}")   #sum funkcija za zbir liste

# ---------------------------------------------------------
# ZADATAK 3: Filtriranje (CONDITIONAL COMPREHENSION)
# ---------------------------------------------------------
# Želimo samo listu ID-jeva kamiona koji su "Active"

# ❌ STARI NAČIN (4 linije)
active_trucks_old = []
for t in trucks:
    if t['status'] == "Active":
        active_trucks_old.append(t['id'])

# ✅ NOVI NAČIN (1 linija)
# [ŠTA_UZIMAM for PREDMET in LISTA if USLOV]
active_trucks = [t['id'] for t in trucks if t['status'] == "Active"]

print(f"Aktivni kamioni:  {active_trucks}")

# ---------------------------------------------------------
# BONUS: High Value Loads (Kombinacija)
# ---------------------------------------------------------
# Daj mi zaradu samo za ture koje su duže od 1000 milja
high_value_revenues = [m * rate for m in miles_list if m > 1000]

print(f"Zarada od dugih tura (>1000mi): {high_value_revenues}")