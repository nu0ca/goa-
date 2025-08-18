#davaleba1
#კომენტარების სახით თავიდან ახსენით რა არის conditional statement, რა დანიშნლება გააჩნიათ და როგორი სახის განცხადებები გვაქვს.
#conditional statement-->არის პირობითი განცხადებები
#დანიშნულება-->გადაწყვეტილების მიღება პროგრამაში
#სახეები--> if, else

#davaleba2
#for ციკლის მეშვეობით გამოიტანეთ "hello world" 50-ჯერ.
for i in range(50):
    print("heloo world")

#davaleba3
#while ციკლის მეშვეობით გამოიტანეთ რიცხვები 3-დან 17-ის ჩათვლით.
i=3
while i<18:
     print(i)
     i=i+1
    
#davaleba3
#while ციკლის მეშვეობით გამოიტანეთ რიცხვები 3-დან 17-ის ჩათვლით.
i=3
while i<18:
     print(i)
     i=i+1

#davaleba4
#მომხმარებელს შემოატანინეთ პაროლი, შემდეგ კი შედეგი შეინახეთ ცვლადში. შექმენით პირობა თუ ის უდრის "1234"-ს დაბეჭდეთ "Password is correct", სხვა შემთხვევაში დაბეჭდეთ "Password is incorrect".
password=input("enter your password:")
if password==1234:
     print("password is corect")
else:
     print("password is incorrect")
    
#davaleba5
#შექმენით ცვლადი სადაც შეინახავთ მომხმარებლის მიერ შემოყვანილი ცხოველის სახეობას. თუ სახეობა უდრის "ძაღლი" დაბეჭდეთ "woaf! woaf!", სხვა შემთხვევაში "შენ არ გყავს ძაღლი"
animal=input("enter your animal breed")
if animal=="ძაღლი":
     print("woaf! woaf!")
else:
     print("შენ არ გყავს ძაღლი")

