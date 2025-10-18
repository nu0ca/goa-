#davaleba1
#შექმენით სია -->  ["ina" , "givi" , "nika" , "daviti" , "ia" , "lizi"] , თქვენი დავალებაა რომ პირველი 2 ელემენტი ჩაანაცვლოთ შემდეგი სიით --> ["irina" , "milana" , "kira", "mate"] //////////////// და ასევე სიის ბოლო ორი ელემენტი შეანაცვლე შემდეგი სიით --> ["gia" , "emzari" , "xvicha"] ამის შემდეგ დაპრინტეთ საბოლოო სია
list =["ina" , "givi" , "nika" , "daviti" , "ia" , "lizi"]
list[0:2]=["irina" , "milana" , "kira", "mate"]
list[4:]=["gia" , "emzari" , "xvicha"] 
print(list)

#davaleba2
#შექმენით ცვლადი და მომხმარებელს შემოატანინეთ რიცხვი,თუ რიცხვი ლუწია დაუპრინტეთ "EVEN" შემდეგ შეამოწმეთ თუ რიცხცვი არის კენტი დაუპრინტეთ "Odd"
number=int(input("choose any number: "))
if number % 2==1:
    print("this number is odd")
elif number%2==0:
    print("this number is Even")
