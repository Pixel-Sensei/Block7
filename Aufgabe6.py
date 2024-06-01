# Aufgabe 6 - Eingabesequenz
werte = input("Geben Sie eine durch Kommas getrennte Ganzzahlsequenz ein:\n")  # Eingabe der Ganzzahlsequenz
meine_liste = werte.split(",")  # Aufteilen der Eingabe in eine Liste von Zeichenketten
for i in range(len(meine_liste)):  # Durchlaufen der Liste
    meine_liste[i] = int(meine_liste[i])  # Umwandeln der Zeichenketten in Ganzzahlen
print(meine_liste)  # Ausgabe der Liste
print(type(meine_liste[0]))  # Ausgabe des Typs des ersten Elements der Liste