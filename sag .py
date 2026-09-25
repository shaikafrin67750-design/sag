# SAG Calculator for Transmission Line

print("===== SAG CALCULATOR =====")

w = float(input("Enter conductor weight (N/m): "))
L = float(input("Enter span length (m): "))
T = float(input("Enter conductor tension (N): "))

# Calculate sag
sag = (w * L ** 2) / (8 * T)

print("\n===== RESULT =====")
print("Conductor Sag =", round(sag, 3), "m")