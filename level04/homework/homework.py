#davaleba 1
# კომენტარების სახით ახსენით რა არის input-ი და output-ი, მოიყავნეთ შესაბამისი მაგალითები.

# input -->მნიშვნელობა რომლის შემოტანა შეგვიძლია და მისი შემდეგ დამუშავება.
#output -->უკუკავშირი,რომელზეც ვღებულობთ პასუხს შესაბამის შემოტანილ მნიშვნელობაზე.


#დავალება 2
# შექმენით ცვლადი, რომელშიც შეინხავთ input ინსტრუქციით შემოტანილ მნიშვნელობას, შემდეგ შეამოწმებთ თუ რა ტიპის მონაცემი ინახება ამ ცვლადში და დაპრინტავთ.
name=input("enter your name:")
print(type(name))



#davaleba 3
# თიოთეული მონაცემთა ტიპისთვის (str,int,float), შექმენით 5 ცვლადი და დაუწერეთ კომენტარი თუ რომელ მონაცემთა ტიპს ინახავს ცვლადი.
#ეს ხუთი ცვლადი მიეკუთნება მონაცემტა ტიპ string_ს
name1="taso"
name2="ana"
name3="nuca"
name4="mariami"
name5="barbare"

#ეს ხუთი ცვლადი მიეკუთნება მონაცემთა ტიპ integer_ს
num1=15
num2=20
num3=56
num4=60
num5=50

#ეს ხუთი ცვლადი მიეკუთნება მონაცემთა ტიპ float_ს
num6=45
num7=23
num8=18
num9=90
num10=77



#davaleba 4
#აიღეთ 3 ცვლადი, შეინახეთ განსხავებული მონაცემთა ტიპები (str,int,float), შემდეგ type ინსტრუქციის გამოყენებით შეამოწმეთ, თუ რომელ მონაცემთა ტიპს ინახავს ცვლადი.
name="mari"
age=15
height=1.80

print(type(name))
print(type(age))
print(type(height))


#davaleba 5
#მომხმარებელს შემოატანინეთ ორი სიტყვა, შეინახეთ ისინი ცვლადებში, მოახდინეთ მათი კონკატინაცია და დაბეჭდეთ.

name1="ana"
name2="maria"
print(name1+name2)



#davaleba 6
# მომხმარებელს შემოატანინეთ 5 რიცხვი სხვადასხვა დამოუკიდებელი input-ების სახით, თქვენი დავალებაა დაბეჭდოთ მათი საშუალო არითმეტიკული.
num1=input("first")
num2=input("seqond")
num3=input("sird")
num4=input("meotxe")
num5=input("mexute")

print((int(num1)+int(num2)+int(num3)+int(num4)+int(num5))/5)


#davaleba 7
#მომხმარებელს შემოატანინეთ სახელი, გვარი, ასაკი, სიმაღლე, წონა და ამ მონაცემების გამოყენებით დაბეჭდეთ ერთი დიდი წინადადება.
name="nuca"
surname="digmelashvili"
age=15
height=1.60
weight=45

print=(name+surname+str(age)+str(height)+str(weight))



