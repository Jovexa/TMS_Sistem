# Day 3 VIN Decoder Tool
# This tool cleans and analyzes Vehicle Identification Numbers (VINs)

print("--- TMS VIN DECODER TOOL ---")

#1. UNOS (Simuliramo dispecera koji unosi aljkavo VIN)
# Primer: " 1hgbh41jXmn109186 "
raw_vin = input("Unesi VIN broj (17 karaktera): ")

#2. CISCENJE PODATAKA ( String metode za ciscenje podataka)
# .strip()  - uklanja praznine sa pocetka i kraja stringa, .uper() - pretvara sve karaktere u velika slova, 
# .replace() - zamenjuje karaktere
clean_vin = raw_vin.strip().upper().replace(" ", "")

print(f"\nObrada u toku...'{raw_vin}'  -> '{clean_vin}'")
      
#3. LOGIKA I ANALIZA (Conditionals + Slicing)
if len(clean_vin) == 17:
    print("VIN je validan.")
    
   #Izdvajamo pojedinacne delove VIN-a koristeci slicing
    wmi = clean_vin[0:3]   # World Manufacturer Identifier
    vds = clean_vin[3:9]   # Vehicle Descriptor Section
    serial = clean_vin[-6:]  # Vehicle Identifier Section (Serijski broj)

   # Izveštaj
    print("-" * 30) # Ovo štampa crtu 30 puta
    print(f"Proizvođač ID: {wmi}")
    print(f"Specifikacija: {vds}")
    print(f"Serijski broj: {serial}")
    print("-" * 30)

else:
    print("GRESKA: VIN mora imati tacno 17 karaktera. Pokusajte ponovo.")   
    print(f"Ocekivano 17 karaktera, dobijeno: {len(clean_vin)}"
          )
 