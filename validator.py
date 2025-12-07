# DAY 11: Load Validator (Advanced Functions)
# Učimo: Defaults, Keywords, Scope

print("--- TMS LOAD VALIDATOR v2.0 ---")

# --- 1. GLOBALNA PROMENLJIVA (The Yard) ---
# Ovo svi vide. Obicno se pisu VELIKIM SLOVIMA.
COMPANY_NAME = "EAGLE FREIGHT INC." 

def get_company_header():
    # Ova funkcija vidi globalnu promenljivu
    return f"Validaciju vrši: {COMPANY_NAME}"

# --- 2. DEFAULT PARAMETERS (Standardna oprema) ---

def check_weight(weight, limit=80000):
    """
    Proverava težinu.
    Ako korisnik NE unese limit, podrazumeva se 80,000 lbs.
    """
    if weight > limit:
        return False, f"❌ PRETEŽAK! ({weight} > {limit})"
    else:
        return True, "✅ Težina OK"

# --- 3. KEYWORD ARGUMENTS & LOGIC ---

def check_rate(rate, miles, min_rpm=2.00):
    """
    Proverava da li se tura isplati.
    Standardni minimum je $2.00 po milji.
    """
    rpm = rate / miles
    
    if rpm < min_rpm:
        return False, f"❌ JEFTINO! (${rpm:.2f}/mi < ${min_rpm}/mi)"
    else:
        return True, f"✅ CENA DOBRA (${rpm:.2f}/mi)"

# --- 4. GLAVNA FUNKCIJA (Orkestrator) ---

def validate_load(load_id, weight, rate, miles, permit=False):
    print(f"\nProvera ture: {load_id}")
    print(get_company_header()) # Zovemo globalni podatak
    
    # PROVERA 1: Težina
    # Pazi ovde! Ako je 'permit' True, povećavamo limit.
    if permit:
        is_weight_ok, msg_weight = check_weight(weight, limit=90000) # Menjamo default!
        print(f"INFO: Koristimo dozvolu za preveliku težinu.")
    else:
        is_weight_ok, msg_weight = check_weight(weight) # Koristimo default (80000)
    
    print(msg_weight)
    
    # PROVERA 2: Cena
    # Ovde koristimo KEYWORD ARGUMENTS da bude jasno šta je šta
    is_rate_ok, msg_rate = check_rate(rate=rate, miles=miles, min_rpm=2.20)
    print(msg_rate)
    
    # FINALNA ODLUKA
    if is_weight_ok and is_rate_ok:
        print(">>> ODLUKA: PRIHVATI TURU! 🚛💨")
    else:
        print(">>> ODLUKA: ODBIJ TURU! 🛑")

# --- TESTIRANJE (Dispečer kuca) ---

# Slučaj 1: Obična tura, dobra cena
validate_load("L-101", 45000, 1500, 600)

# Slučaj 2: Teška tura BEZ dozvole
validate_load("L-102", 82000, 3000, 1000)

# Slučaj 3: Teška tura SA dozvolom (Overweight Permit)
validate_load("L-103", 85000, 4000, 1000, permit=True)
