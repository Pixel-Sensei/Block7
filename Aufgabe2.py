# Aufgabe 2 - Logische Ausdrücke
x = 10  # Initialisierung der Variablen x
print(x > 10)  # Überprüfen, ob x größer als 10 ist (False)
print(not (x > 10))  # Überprüfen, ob x nicht größer als 10 ist (True)
print(x % 2 == 0 and x % 3 > 0)  # Überprüfen, ob x gerade ist und nicht durch 3 teilbar ist (True)
print(not (x % 3 == 0) or x < 10)  # Überprüfen, ob x nicht durch 3 teilbar oder kleiner als 10 ist (True)

# De Morgan's Gesetze
p = False  # Initialisierung der Variablen p
q = True  # Initialisierung der Variablen q
print(not (p and q) == (not p or not q))  # De Morgan's Gesetz überprüfen (True)
print(not (p or q) == (not p and not q))  # De Morgan's Gesetz überprüfen (True)