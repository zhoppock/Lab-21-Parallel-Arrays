# JumpinJava.py - This program looks up and prints the names and prices of coffee orders.  
# Input:  Interactive
# Output:  Name and price of coffee orders or error message if add-in is not found 

# Declare variables.
NUM_ITEMS = 5 # Named constant
addTotal = 0
# Initialized list of add-ins
addIns = ["Cream", "Cinnamon", "Chocolate", "Amaretto", "Whiskey"]

# Initialized list of add-in prices
addInPrices = [.89, .25, .59, 1.50, 1.75]
foundIt = False # Flag variable
orderTotal = 2.00  # All orders start with a 2.00 charge

# Get user input
addIn = input("Enter coffee add-in or XXX to quit: ")

# Write the rest of the program here.
while addIn != "XXX":
  sub = 0
  while sub < NUM_ITEMS and foundIt == False:
    if addIn == addIns[sub]:
      foundIt = True
      price = addInPrices[sub]
    sub += 1
  if foundIt == True:
    print(addIn,"Price is $"+ str(price))
    addTotal = addTotal + price
  else:
    print("Sorry, we do not carry that.")
  addIn = input("Enter another coffee add-in or XXX to quit: ")
  foundIt = False
orderTotal = orderTotal + addTotal
print("Order Total is $" + str(orderTotal))
