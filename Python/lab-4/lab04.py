Product_Name = input("Enter Product Name : ")
Price = float(input("Enter Price        : "))
Quantity = int(input("Enter Quantity     : "))

Total_Price = Price * Quantity

Amount_Str = str(Total_Price)


print("------------------------------------------")
print( "    TYPE CASTING SUMMARY        ")
print("------------------------------------------")

print(f"Variable        Value          Python Type")
print("------------------------------------------")
print(f"product_name    {Product_Name}          {type(Product_Name)}")
print(f"price           {Price}          {type(Price)}")
print(f"quantity        {Quantity}             {type(Quantity)}")
print(f"total_price     {Total_Price}          {type(Total_Price)}")
print(f"amount_str      {Amount_Str}          {type(Amount_Str)}")


print("------------------------------------------")
print("           TAX INVOICE           ")
print("------------------------------------------")

print(f"Product Name    : {Product_Name}")
print(f"Price per Unit  : Rs. {Price}")
print(f"Quantity        : {Quantity}")
print("------------------------------------------")
print(f"Invoice Total   : Rs. {Amount_Str}")
print("==========================================")