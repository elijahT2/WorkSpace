"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
charge= 35.00
# Number of characters.
num_Chars = int(input("Enter the number of characters on the sign: "))
# Color of characters.
color = input("Enter the color of the characters (gold/black/white): ").lower()
# Type of wood.
wood_type = input("Enter the type of wood (oak/pine): ").lower()
# Write assignment and if statements here as appropriate.
if num_Chars > 5:
    charge += (num_Chars - 5) * 4
    
if wood_type == "oak":
      charge += 20.00

if color == "gold":
    charge += 15.00

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
