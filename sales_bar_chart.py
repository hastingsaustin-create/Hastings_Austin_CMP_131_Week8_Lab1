#Austin Hastings
#CMP 131 86520
#Week 8
#Lab 1
#29 OCT 2026
#Sales Chart
print("Sales Chart")
print("-----------")

ast =""
store = int(input("Enter number of stores: "))

for i in range (store):
    sale = int(input("Enter toady's sales for store: " + str(i+1)+ ":"))

    for j in range (sale):
        ast = ast + "*"
    ast = ast + "/n"
print(ast)