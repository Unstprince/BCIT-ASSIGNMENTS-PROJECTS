x = 12
y = 25
xy = 25 + 12
print(xy)

name = input("My name is: ")
age = int(input("My age is: "))
print(f"my name is {name}, i am {age} years old")

Country = input("Enter Your Country Name: ").strip().lower()
if Country == "south africa":
    print(f"{Country.title()} - The Sambas of Africa")
elif Country == "nigeria":
    print(f"{Country.title()} - Giant Of Africa")
elif Country == "cameroon":
    print(f"{Country.title()} - The Lions OF Africa")
elif Country == "angola":
    print(f"{Country.title()} - The Heartbeat Of Africa")
elif Country == "zimbabwe":
    print(f"{Country.title()} - The Breath OF Africa")
elif Country == "morocco":
    print(f"{Country.title()} - The light of Africa")
else:
    print("You don't belong Here")