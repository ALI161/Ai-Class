age = int(input("Enter your age: "))
day = input("Enter the day: ")

if age < 5:
    price = 0
elif age <= 12:
    price = 50000
elif age >= 60:
    price = 60000
else:
    price = 100000

if day == "tuesday":
    discount = price * 0.2
    price = price - discount

print("Age:", age)
print("Day:", day)

if price == 0:
    print("Free entry!")
else:
    print("Ticket price:", int(price), "Toman")
