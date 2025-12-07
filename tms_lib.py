# FAJL: tms_lib.py
# Backend logika za TMS v0.2

def create_truck(truck_id, model, status="Available"):
    """Pravi novi profil kamiona."""
    return {
        "id": truck_id,
        "model": model,
        "status": status,
        "miles": 0,
        "revenue": 0.0
    }

def add_revenue(truck, amount):
    """Dodaje zaradu kamionu."""
    truck["revenue"] += amount
    return truck

def get_active_trucks(fleet):
    """
    Vraća samo aktivne kamione koristeći List Comprehension!
    (Dan 13 Lekcija)
    """
    return [t for t in fleet if t["status"] == "Available"]

def calculate_total_revenue(fleet):
    """
    Računa ukupan promet cele flote u jednoj liniji.
    (Dan 13 Lekcija)
    """
    all_revenues = [t["revenue"] for t in fleet]
    return sum(all_revenues)

def show_fleet_report(fleet):
    """Pravi lep ispis cele flote."""
    print(f"\n{'ID':<10} {'MODEL':<15} {'STATUS':<12} {'REVENUE':<10}")
    print("-" * 50)
    for t in fleet:
        print(f"{t['id']:<10} {t['model']:<15} {t['status']:<12} ${t['revenue']:.2f}")
    print("-" * 50)