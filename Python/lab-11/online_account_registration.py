
username=input("Enter a username : ")
password=input("Enter a password : ")


print("================================================")
f_uppercase=False
f_digit=False

for ch in password:
    if ch.isupper():
        f_uppercase=True
    elif ch.isdigit():
        f_digit=True

print("----RESULT-----")

if  f_digit and f_uppercase and len(password)>=8:
        print(f"Password is VALID ! \n Account created successfully for {username} !")
else:
    print("inalid password")

print("================================================")
           
    