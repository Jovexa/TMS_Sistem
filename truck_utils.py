# FAJL: truck_utils.py
# Svrha: Funkcije vezane samo za kamione

def create_truck(truck_id, status="Available"):
    """Pravi rečnik (profil) za novi kamion."""
    return {
        "id": truck_id,
        "status": status,
        "total_miles": 0
    }

def update_status(truck_dict, new_status):
    """Menja status kamiona (npr. u 'On Load')."""
    truck_dict["status"] = new_status
    return truck_dict

def get_truck_info(truck_dict):
    """Vraća lep ispis informacija."""
    return f"🚛 Kamion {truck_dict['id']} | Status: {truck_dict['status']}"