# GOA bank_ის პროექტი
print("Welcome to GOA Bank!")
input("Press Enter to start registration")

print("Registration Form")

# მომხმარებლის მონაცემების შეყვანა
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
user_id = input("Enter your ID: ")

# პაროლის შემოწმება while ციკლით
while True:
    password = input("Enter your password: ")
    confirm_password = input("Repeat password: ")
    
    # თუ პაროლები ემთხვევა, ციკლი შეწყდება
    if password == confirm_password:
        print("Password saved successfully!")
        break# ციკლის შეწყვეტა

    else:
        # თუ პაროლები არ ემთხვევა, მომხმარებელს დაეცემა შეტყობინება
        print("Passwords do not match, try again.")

# სტატუსის არჩევა
print("Choose your status:")
print("1 - Pupil")
print("2 - Student")
choice = input("Enter number: ")

# სტატუსის შენახვა
if choice == "1":
    status = "Pupil"
else:
    status = "Student"

# რეგისტრაციის შედეგების ჩვენება
print(" Registration completed!")
print("First Name:", first_name)
print("Last Name:", last_name)
print("ID:", user_id)
print("Status:", status)

# რეგისტრაციის დასასრული
print("Thank you for using GOA Bank!")




