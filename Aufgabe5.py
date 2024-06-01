# Aufgabe 5 - Daten aus dem Wörterbuch
alter_einkommen = {"Joe": [32, 14500],  # Initialisierung des Wörterbuchs mit Alter und Einkommen
                   "Emily": [27, 13000],
                   "George": [58, 22000],
                   "Michael": [42, 27000],
                   "Lois": [39, 23000]
                  }

# Jüngster Mitarbeiter
jüngster = 10000  # Initialisierung mit einem hohen Wert für Vergleichszwecke
jüngste_person = ""  # Initialisierung der Variablen für die jüngste Person
schlüssel_liste = list(alter_einkommen.keys())  # Liste der Schlüssel (Namen) im Wörterbuch
wert_liste = list(alter_einkommen.values())  # Liste der Werte (Alter und Einkommen) im Wörterbuch
for i in wert_liste:  # Durchlaufen der Werteliste
    if i[0] < jüngster:  # Prüfen, ob das aktuelle Alter kleiner ist als das gespeicherte jüngste Alter
        jüngster = i[0]  # Aktualisierung des jüngsten Alters
        jüngste_person = schlüssel_liste[wert_liste.index(i)]  # Aktualisierung der jüngsten Person
print(jüngste_person, "ist der jüngste.")  # Ausgabe der jüngsten Person

# Mitarbeiter mit dem besten Gehalt
gehalt = 0  # Initialisierung mit einem niedrigen Wert für Vergleichszwecke
beste_gehalts_person = ""  # Initialisierung der Variablen für die Person mit dem besten Gehalt
schlüssel_liste = list(alter_einkommen.keys())  # Liste der Schlüssel (Namen) im Wörterbuch
wert_liste = list(alter_einkommen.values())  # Liste der Werte (Alter und Einkommen) im Wörterbuch
for i in wert_liste:  # Durchlaufen der Werteliste
    if i[1] > gehalt:  # Prüfen, ob das aktuelle Gehalt größer ist als das gespeicherte beste Gehalt
        gehalt = i[1]  # Aktualisierung des besten Gehalts
        beste_gehalts_person = schlüssel_liste[wert_liste.index(i)]  # Aktualisierung der Person mit dem besten Gehalt
print(beste_gehalts_person, "hat das beste Gehalt.")  # Ausgabe der Person mit dem besten Gehalt

# Durchschnittsalter
durchschnitt = 0  # Initialisierung der Summe für das Durchschnittsalter
for i in alter_einkommen.values():  # Durchlaufen der Werte im Wörterbuch
    durchschnitt += i[0]  # Addieren des Alters zur Summe
durchschnitt /= len(alter_einkommen)  # Berechnung des Durchschnitts
print("Das Durchschnittsalter in der Firma ist ", durchschnitt, ".", sep="")  # Ausgabe des Durchschnittsalters

# Durchschnittsgehalt
durchschnitt = 0  # Initialisierung der Summe für das Durchschnittsgehalt
for i in alter_einkommen.values():  # Durchlaufen der Werte im Wörterbuch
    durchschnitt += i[1]  # Addieren des Gehalts zur Summe
durchschnitt /= len(alter_einkommen)  # Berechnung des Durchschnitts
print("Das Durchschnittsgehalt in der Firma ist ", durchschnitt, ".", sep="")  # Ausgabe des Durchschnittsgehalts
