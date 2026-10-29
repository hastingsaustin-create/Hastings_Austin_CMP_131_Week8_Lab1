#Austin Hastings
#CMP 131 86520
#Week 8
#Lab 1
#29 OCT 2026
#Sales Chart
print("Sales Chart")
print("-----------")

for store in (1, 2, 3, 4, 5):
    sales = float(input(f"Enter the sales for store {store}: "))

    while sales <0:
        print("Sales cannot be a negative number")
        sales = float(input(f"Enter the sales for store {store}: "))
