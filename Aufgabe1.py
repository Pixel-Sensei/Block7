# Aufgabe 1 - Ziegelpyramide
ziegel = int(input("Geben Sie die Anzahl der Ziegel ein, die wir haben:\n"))  # Eingabe der Anzahl der verfügbaren Ziegel
höhe = 0  # Initialisierung der Höhe der Pyramide
while ziegel > 0:  # Schleife läuft, solange Ziegel verfügbar sind
    if ziegel >= höhe + 1:  # Prüfen, ob genügend Ziegel für die nächste Schicht vorhanden sind
        ziegel -= höhe + 1  # Ziegel für die aktuelle Schicht verbrauchen
        höhe += 1  # Höhe der Pyramide erhöhen
    else:
        break  # Schleife beenden, wenn nicht genügend Ziegel vorhanden sind
print("Die Höhe der Pyramide ist:", höhe)  # Höhe der Pyramide ausgeben
print("Wir haben", ziegel, "Ziegel übrig, nachdem wir sie gebaut haben.")  # Übrige Ziegel ausgeben
