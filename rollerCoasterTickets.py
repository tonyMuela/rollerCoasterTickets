print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you? "))
    if age >= 18:
        bill = 12
        print("Adult tickets are $12")
    elif age >= 12 <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 5
        print("Child tickets are $5")

    wants_photo = input("Would you like to buy a picture? Y / N ").upper()

    if wants_photo == "Y":
        bill += 3
        print("That'll an additional $3")

    else:
        print("Wow, I guess family memories don't mean anything to you.")

    print(f"Your total bill is ${bill}")

else:
    print("Get rekt shorty")
