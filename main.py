from house import Rent, Housemate
from reports import PdfReport, FileSharer

# Asking for information regarding the rent and period
amount = float(input("Hello! Please enter the total rent amount: "))
period = input("What is the period? (ex: January 2020): ")
total_people = int(input("How many total people (up to 5) share the rent? "))

# Asking for the user's name and information
name = input("What is your name? ")
room_size = float(input(f"What is the room size of {name} in square feet? "))

# Generate a list to append all housemates, including the user
housemates = []
housemates.append(Housemate(name, room_size))

# Ask for each subsequent housemate, and add that housemate to our list
for i in range(total_people-1):
    housemate_name = input("Enter the name of a housemate: ")
    housemate_room_size = float(input(f"What is the room size of {housemate_name} in square feet? "))
    housemates.append(Housemate(housemate_name, housemate_room_size))

# Closing message
print("Please check the generated report for your calculated rent amounts. Thank you!")

# Generate the report
the_rent = Rent(amount, period)
pdf_report = PdfReport(filename=f"{the_rent.period}.pdf")
pdf_report.generate(the_rent, housemates)

# Share the report
# Only used for Repl.it; Uncomment below 2 lines if applicable):
# file_sharer = FileSharer(filepath=pdf_report.filename)
# print(file_sharer.share())