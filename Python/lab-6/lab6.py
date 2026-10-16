Customer_Name = input("Enter Customer Name: ")
Garment_Name = input("Enter Garment Name: ")
Price = float(input("Enter Price of one garment: "))
Quantity = int(input("Enter Number of Garments: "))

Total_Amount = Price * Quantity


print(f"==========================================")
print(f"                  BILL")
print(f"==========================================")

print(f"Customer Name : {Customer_Name}")
print(f"Garment Name  : {Garment_Name}")
print(f"Price per Unit: Rs. {Price}")
print(f"Quantity      : {Quantity}")
print(f"Total Amount  : Rs. {Total_Amount}")

print(f"==========================================")
