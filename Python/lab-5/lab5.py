import math



Value = float(input("Enter a numerical value: "))
Exponent = float(input("Enter an exponent: "))
Decimal_Measurement = float(input("Enter a decimal measurement: "))

Power = math.pow(Value, Exponent)
Square_Root = math.sqrt(Value)
Ceil_Value = math.ceil(Decimal_Measurement)
Floor_Value = math.floor(Decimal_Measurement)


print("--- Results ---")

print(f"Value             : {Value}")
print(f"Exponent          : {Exponent}")
print(f"Power (pow)       : {Power}")
print(f"Square Root (sqrt): {Square_Root:.4f}")
print(f"Decimal Value     : {Decimal_Measurement}")
print(f"Ceil Value        : {Ceil_Value}")
print(f"Floor Value       : {Floor_Value}")
print("==========================================")
