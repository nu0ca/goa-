#davaleba1
#მომხმარებელს შემოატანინეთ ორი რიცხვი,შეამოწმეთ თუ პირველი რიცხვი მეტია მეორე რიცხვზე დაპრინტე რომ ‘first is more than second’,ასევე შეამოწმე თუ პირველი რიცხვი ნაკლებია მეორე რიცხვზე დაპრინტე რომ ‘first is less than second’ და სხვა დანარჩენ შემთხვევაში დაპტინტე რომ ‘first number equal to second number’

num1=input("enter your number: ")
num2=input("enter your number: ")

if num1>num2:
    print("first is more than second")
elif num1<num2:
    print("first is less than second")
else:
    print("first number equal to second number")

#davaleba2
#მომხმარებელს შემოატანინე რაიმე სტრინგი,ასევე შექმენი ცვლადი სადაც შეინახავთ თქვენს სახელს,შემდეგ შეამოწმე თუ მომხმარებლის შემოყვანილი სტრინგი უდრის შენა სახელს დაუპრინტე რომ ‘სეხნიები ვართ’ სხვა შემთხვევაში დაუპრინტეთ რომ ‘სხვადასხვა სახელები გავქვს’

name1=str(input("enter your name: "))
name2="nuca"

if name1==name2:
    print("sexniebi vart")
else:
    print("sxvadasxva saxelebi gvaqvs")

#davaleba3
#შექმენი ორი ცვლადი სადაც შეინახავთ ინტეჯერ ტიპოს მონაცემებს,თქვენი დავალებაა შეამოწმოთ,თუ პირველი რიცხვი მეტია 0 ზე და და მეორე რიცხვიც მეტია 0 ზე დაუპრინტე რომ ‘ორივე რიცხვი დადებითია, ასევე შეამოწმე თუ პირველი რიცხვი ნაკლებია 0 ზე და მეორე რიცხვიც ნაკლებია 0 ზე დაპურინტე რომ  ‘ორივე რიცხვი არის უარყოფით’,სხვა დანარჩენ შემთხვევაში დაუპრინტე რომ ‘ეს რა ჯანდაბაა’

num1=int(input("enter your age: "))
num2=int(input("enter your age: "))

if num1>0 and num2>0:
    print("ორივე რიცხვი დადებითია")
elif num1<0 and num2<0:
    print("ორივე რიცხვი არის უარყოფით")
else:
    print("ეს რა ჯანდაბაა")

#davaleba4
#დაატრიალეთ ფორ ლუპი 50 დან 100 მდე 2 ის გამოტივებით
for i in range(50,100,2):
    print(i)

#davaleba5
#ვაილ ლუპის გამოყენებით 20 დან 40 მდე გამოიტანეთ ყველა რიცხვი
i=20
while i<40:
    print(i)
    i=i+1

