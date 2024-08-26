print("Hello people!\nwelcome to the bill calculator which helps you to split the bill within your people")
amount =float(input("What is the total amount? $"))
tip = int(input("How much you want to tip to the waiter 10,12 or 15? "))
member =int(input("How many member were you there? "))

total_amount = amount + (amount * tip / 100)

final_amount = round(total_amount,2)

print(f"Each person shoud pay ${final_amount}")


            