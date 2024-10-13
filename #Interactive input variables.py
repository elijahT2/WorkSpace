#Interactive input variables

name = input("Enter Employee’s name: ")
shifts = int(input("Enter Number of Shifts: "))
transactions = int(input("Enter Number of Transactions: "))
transaction_value = float(input("Enter Transaction Dollar Value: "))
#calculation for productivity score
score = (transaction_value / transactions) /shifts

#nested if statement
if score <= 30:
    bonus = 50.00
elif 31 <= score <= 69:
    bonus = 75.00
elif 70 <= score <= 199:
    bonus = 100.00
else:
    bonus = 200.00

print("Employee Name: " + name)
print(f"Employee Bonus: ${bonus:.2f}")
