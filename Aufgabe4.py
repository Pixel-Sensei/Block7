# Aufgabe 4 - Bitverschiebung
num_1 = 42  # 101010 in Binär
num_2 = 63  # 111111 in Binär
print("Die erste Zahl ist", num_1, "und ihr Binärwert ist", bin(num_1)[2:])  # Ausgabe der ersten Zahl und ihres Binärwerts
print("Die zweite Zahl ist", num_2, "und ihr Binärwert ist", bin(num_2)[2:])  # Ausgabe der zweiten Zahl und ihres Binärwerts
num_1 >>= 2  # Rechtsverschiebung von num_1 um 2 Bits
num_2 <<= 3  # Linksverschiebung von num_2 um 3 Bits
print("Die erste Zahl ist", num_1, "nach rechts Verschieben um 2 und ihr Binärwert ist", bin(num_1)[2:])  # Ausgabe der ersten Zahl nach der Verschiebung
print("Die zweite Zahl ist", num_2, "nach links Verschieben um 3 und ihr Binärwert ist", bin(num_2)[2:])  # Ausgabe der zweiten Zahl nach der Verschiebung
