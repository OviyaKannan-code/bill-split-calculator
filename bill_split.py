print("--- Bill Split Calculator ---")
bill = float(input("Total Bill Amount: "))
tips = float(input("Tip Percentage (%): "))
person = int(input("Number of Persons: "))
tip_amount = (tips / 100) * bill
total = tip_amount + bill
per_person = total / person
print(f"\nTotal (including tip): Rs.{total:.2f}")
print(f"Each person pays: Rs.{per_person:.2f}")