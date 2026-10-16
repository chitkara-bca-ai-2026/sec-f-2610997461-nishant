t_fee=int(input("enter tuition fee :"))
l_fee=int(input("enter lab fee"))
lib_fee=int(input("enter your library fee :"))
exam_fee=int(input("enter exam fee :"))
dis=int(input("enter discount amount :"))

print("................................................................")
add=t_fee+l_fee+lib_fee+exam_fee
after_dis=add-dis

annual_fee=after_dis*2
monthly_fee=annual_fee/12

print(f"Tuition fee         : {t_fee:.1f}")
print(f"Lab fee             : {l_fee:1f}")
print(f"library fee         :{lib_fee:.1f}")
print(f"exam fee            : {exam_fee:.1f}")
print(f"Total fee           : {add:.1f}")
print(f"Discount            : {dis:.1f}")
print(f"fee after discount  : {after_dis:.1f}")
print(f"Annual fee          : {annual_fee:.1f}")
print(f"Monthly Installment : {monthly_fee:.2f}")

