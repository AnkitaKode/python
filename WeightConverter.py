weight =int(input("Enter your weight in kg"))
unit = input("L(bs) or K(gs)")
unit.upper()

if unit=="L":
    converted=0.45*weight
    print(f"You are {converted} kilos")

else:
    converted=weight/0.45
    print(f"You are {converted} pounds")
print("Thank You")