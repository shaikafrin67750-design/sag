print("OHM'S LAW CALCULATOR")
print("--------------------")

print("1. Calculate Voltage")
print("2. Calculate Current")
print("3. Calculate Resistance")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    current = float(input("Enter Current (I) in Amperes: "))
    resistance = float(input("Enter Resistance (R) in Ohms: "))
    voltage = current * resistance
    print("Voltage (V) =", voltage, "V")

elif choice == 2:
    voltage = float(input("Enter Voltage (V) in Volts: "))
    resistance = float(input("Enter Resistance (R) in Ohms: "))
    current = voltage / resistance
    print("Current (I) =", current, "A")

elif choice == 3:
    voltage = float(input("Enter Voltage (V) in Volts: "))
    current = float(input("Enter Current (I) in Amperes: "))
    resistance = voltage / current
    print("Resistance (R) =", resistance, "Ohms")

else:
    print("Invalid choice!")
