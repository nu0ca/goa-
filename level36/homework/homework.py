#davaleba1
# მომხმარებელს შემოატანინეთ სიტყვა.  
# -> იტერაციით გაიარეთ თითო ასო  
# -> თუ შეხვდებით ასო 'e'-ს ან 'E'-ს გაჩერდით (break)  
# -> დაბეჭდეთ მხოლოდ ის ასოები, რაც მანამდე იყო  
text = input("შეიყვანეთ ტექსტი: ")

for i in text:
    print(i)
    if i == "e" or i == "E":
        break
   
#დავალება2
word=input()
if "bad" in word:
    print("აკრძალული სიტყვა")
else:
    print("ყველაფერი რიგზეა")

#დავალება3
word=input("შემოიყვანე წინადადება")
for i in word:
    if i=="":
        continue
    print(i)

#davaleba4
word=input("შეიყვანე წინადადება:")
result=""
for i in word:
    if i in["a","e","i","o","u"]:
        continue
    result+=i
print(result)


#davaleba5
num1=int(input("enter your first number:"))
num2=int(input("enter your second number:"))
for i in range(num1,num2):
    if i%15==0:
        print(i)
        break
#davaleba6
while True:
    word=input("ჩაწერე რამე პითონზე:")
    if word=="pyton is best":
        break
    print("you shoud learn pyton")

#davaleba7
num1=int(input("enter your first number:"))
num2=int(input("enter your second number:"))
for i in range(num1,num2):
    if i%3==0:
        print(i)
        break
    



