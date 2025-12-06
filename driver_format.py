# day 4: Driver Name Formatter & Email Generator
#Cilj Nauciti split() metodu za razdvajanje imena i prezimena

print("---SISTEM ZA REGISTRACIJU VOZACA---")

#1. INPUT
#Oxekujemo da korisnik unese puno ime i prezime SA razmakom izmedju
# Primer unosa: " marko markovic "
raw_name = input("Unesi puno ime i prezime vozaca: ")

#2. CLEANING (Osnovno ciscenje podataka)
# .strip() - uklanja praznine sa pocetka i kraja stringa
clean_name = raw_name.strip()

#3. Spliting (Razdvajanje imena i prezimena) kljucna lekcija danas
# . split() - razdvaja string na delove koristeci razmak kao podrazumevani separator
name_parts = clean_name.split()

# name_parts je sada lista delova imena, npr. ["marko", "markovic"]
# name_parts[0] je ime, name_parts[1] je prezime

first_name = name_parts[0].capitalize()  # Prvo ime sa velikim pocetnim slovom
last_name = name_parts[1].capitalize()   # Prezime sa velikim pocetnim slovom

#4. Generisanje novih podataka
#pravimo sluzbeni email koristeci ime i prezime vozaca: marko.markovic@tms-logistics.com
#Koristimo .lower() metodu da sve pretvorimo u mala slova
company_email = f"{first_name.lower()}.{last_name.lower()}@tms-logistics.com"

#Pravimo Display Name za vozaca (Puno ime sa velikim pocetnim slovima)
#. title() metoda pretvara prvo slovo svake reci u veliko slovo ali ovde vezbamo spajanje onoga sto smo vec napravili
display_name = f"{first_name} {last_name}"

#5. OUTPUT (Prikaz rezultata)
print("\n---NOVI PROFIL VOZACA KREIRAN---")
print(f"ID Kartica: {display_name}")  # Markovic, Marko
print(f"Ime:        {first_name}")        # Marko
print(f"Prezime:    {last_name}")         # Markovic
print(f"Sluzbeni Email: {company_email}")  
print("-" * 35)

#BONUS: Provera da li je uneo i ime i prezime
print(f"(Debug info: Pronadjeno {len(name_parts)} reci u imenu)")



