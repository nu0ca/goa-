#davaleba1
# შემოატანინეთ მომხმარებელს 3 რიცხვი, შეამოწმეთ:
# თუ 1 და 2 რიცხვი ტოლია -> დაწერეთ 1 და 2 ტოლია
# თუ 1 და 3 რიცხვი ტოლია -> დაწერეთ 1 და 3 ტოლია
# თუ 2და 3 რიცხვი ტოლია -> დაწერეთ 2და 3 ტოლია
# თუ სამივე ტოლია -> დაწერეთ სამივე ტოლია
# თუ არცერთი არ არის ტოლი -> დაწერეთ არცერთი არ არის ტოლია
num1=input("enter your number")
num2=input("enter your number")
num3=input("enter your number")
if num1==num2:
    print("1 და 2 ტოლია")
elif num1==num3:
    print("1 და 3 ტოლია")
elif num2==num3:
    print("2და 3 ტოლია")
elif num1==num2 or num1==num3 or num2==num3:
    print("სამივე ტოლია")
else:
    print("არცერთი არ არის ტოლია")

#davaleba2
# შემოატანინეთ მომხმარებელს რიცხვი 1-დან 12ჩათვლით:
# თუ ეს რიცხვი არის 12, 1, 2 -> დაპრინტეთ ზამთარი
# თუ ეს რიცხვი არის 3, 4, 5 -> დაპრინტეთ გაზაფხული
# თუ ეს რიცხვი არის 6, 7, 8 -> დაპრინტეთ ზაფხული
# თუ ეს რიხცვი არის 9, 10, 11 -> დაპრინტეთ

month=int(input("შეიყვანე რიცხვი 1-დან 12ჩათვლით:"))
if month==2 or month==1 or month==2:
    print("ზამთარი")
elif month==3 or month==4 or month==5:
    print("გაზაფხული")
elif month==6 or month==7 or month==8:
    print("ზაფხული")
elif month==9 or month==10 or month==11:
    print("შემოდგომა") 
else:
    print("არასწორი რიცხვი")

#davaleba3შემოატანინეთ მომხმარებელს თავისი სახელი:
# თუ სახელი უდრის admin:
#    მოთხოვეთ შემოიყვანოს ადმინის პაროლი:
#       თუ პაროლი უდრის adminpassword123:
#         დაპრინტეთ სალამი ადმინ
#       სხვა შემთხვევაში:
#         დაპრინტეთ წვდომა არ გაქვს
# სხვა შემთხვევაში:
#   დაპრინტეთ სალამი მომხმარებელო

name=input("enter your name:")

if name=="admin":
    password=input("enter your password:")
    if password=="adminpassword123":
        print(" სალამი ადმინ")
    else:
        ("წვდომა არ გაქვს")
else:
    print("სალამი მომხმარებელო")