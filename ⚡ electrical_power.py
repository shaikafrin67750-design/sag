print("ELECTRICAL POWER CALCULATOR")
print("---------------------------")

print("1. Calculate Power")
print("2. Calculate Voltage")
print("3. Calculate Current")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    voltage = float(input("Enter Voltage (V): "))
    current = float(input("Enter Current (A): "))
    power = voltage * current
    print("Electrical Power =", power, "W")

elif choice == 2:
    power = float(input("Enter Power (W): "))
    current = float(input("Enter Current (A): "))
    voltage = power / current
    print("Voltage =", voltage, "V")

elif choice == 3:
    power = float(input("Enter Power (W): "))
    voltage = float(input("Enter Voltage (V): "))
    current = power / voltage
    print("Current =", current, "A")

else:
    print("Invalid choice!")
