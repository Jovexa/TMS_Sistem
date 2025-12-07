# FAJL: load_utils.py
# Svrha: Funkcije za računanje cena i proveru tereta

def calculate_revenue(miles, rate):
    """Računa ukupan prihod."""
    return miles * rate

def verify_weight(weight):
    """Vraća True ako je ispod 80k, inače False."""
    limit = 80000
    if weight > limit:
        return False, f"⚠️ PRETEŽAK ({weight} lbs)"
    return True, "✅ Težina OK"

def format_rate_con(load_id, revenue):
    """Pravi mali izveštaj o ceni."""
    return f"📄 LOAD #{load_id} -> POTVRĐEN IZNOS: ${revenue:.2f}"