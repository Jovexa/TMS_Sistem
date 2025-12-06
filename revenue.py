loads = [1200, 850, 2000, 450]

if not loads:
    print("Nema podataka o turama!")
else:
    total_revenue = sum(loads)
    average_revenue = total_revenue / len(loads)
    print(f"Ukupan promet ove nedelje: ${total_revenue}")
    print(f"Prosečan promet po turi: ${average_revenue:.2f}")
