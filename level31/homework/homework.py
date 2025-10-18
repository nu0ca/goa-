#davaleba1
#მოცემულია სია --> [1, 2, 3, 4, 5, 6]
# შეცვალე შუა ორი ელემენტი რიცხვებით [10, 20, 30].
numbers=[1, 2, 3, 4, 5, 6]
numbers[2:4]=[10, 20, 30]
print(numbers)

#davaleba2
#მოცემულია სია --> ["apple", "banana", "cherry", "kiwi", "mango"]
# შეცვალე პირველი ორი ელემენტი სიით ["pear", "plum"].\
fruit=["apple", "banana", "cherry", "kiwi", "mango"]
fruit[0:2]=["pear", "plum"]
print(fruit)

#davaleba3
#ოცემულია სია --> ["a", "b", "c", "d", "e", "f"]
# შეცვალე ბოლო სამი ელემენტი სიით ["x", "y", "z"].
frr=["a", "b", "c", "d", "e", "f"]
frr[3:]= ["x", "y", "z"]
print(frr)

#davaleba4
# #)მოცემულია სია --> ["red", "green", "blue", "yellow", "black", "white"]
# შეცვალე ინდექსებზე 2-დან 5-მდე ელემენტები სიით ["purple", "orange"]
colors= ["red", "green", "blue", "yellow", "black", "white"]
colors[1:4]=["purple", "orange"]
print(colors)

#davaleba5
#მოცემულია სია --> ["გიორგი" , "ირმა" , "საბა" ]
# შეცვალე მთლიანი სია შემდეგი სიით -->  ["red", "green", "blue", "yellow", "black", "white"]
dd=["გიორგი" , "ირმა" , "საბა" ]
dd[0:]=["red", "green", "blue", "yellow", "black", "white"]
print(dd)

#davaleba6
#მომხმარებელმა შეიყვანოს რიცხვი — შეამოწმე ლუწია თუ კენტი ეს რიცხვი , თუ ლუწია დაპრინტე --> "Even" ,თუ კენტია დაპრინტე --> "Odd".

number=int(input("choose any number: "))
if number%2==1:
    print("this number is ODD")
elif number%2==0:
    print("this number is EVEN")

#davaleba7
#შექმენი სია --> სადაც შეინახავ ინტეჯერებს ,შემდეგ შეამოწმე თუ სიაში მყოფი მე3 ინდექსზე მდგომი ელემენტი არუს ლუწი დაპრინტე --> "Even number" ,თუ სიაში მყოფი მესამე ინდექსზე მდგომი ელემენტი არის კენტი დაპრინტე --> "Odd number"
numbers=[1,2,3,4,5,6,7,8,9]
number1=numbers[3]
if number1%2==1:
    print("this number is ODD")
elif number1%2==0:
    print("this number is EVEN")

#davaleb8
#შექმენი სია სადაც შეინახავ ინტეჯერებს, თუ სიაში მყოფი ბოლო ელემენტი არის ლუწი და მეტი 50 ზე დაპრინტე --> "ეს რიცხვი არის ლუწი და მეტი 50 ზე" , თუ რიცხვი არის კენტი და ნაკლებია 50 ზე დაპრინტე --> "ეს რიცხვი არის კენტი და ნაკლები 50 ზე"
numbers = [1,2,3,4,5,6,7,8,9,10,28,67]
last_num = numbers[-1]
if last_num % 2 == 0 and last_num > 50:
    print("ეს რიცხვი არის ლუწი და მეტი 50 ზე")
elif last_num % 2 ==1 and last_num < 50:
    print("ეს რიცხვი არის კენტი და ნაკლები 50 ზე")

#davaleba9
#შექმენი სია სადაც შეინახავ ინტეჯერებს,თუ სიაში მყოფი მე 5 ინდექსზე მდგომი ელემენტი არის ლუწი ან 100 ზე მეტი დაუპრინტე --> "even or more than 100" ,თუ სიაში მყოფი მესამე ინდექსზე მდგომი ელემენტი არის კენტი ან ნაკლები 100 ზე დაუპრინტე --> odd or less than 100
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,986]
if numbers[5] % 2 == 0 or numbers[5] > 100:
    print("even or more than 100")
if numbers[3] % 2==1 or numbers[3] < 100:
    print("odd or less than 100")

#davaleba10
#შექმენი ორი ცვლადი სადაც შეინახავთ სტრინგებს , შემდეგ შეადარე უდრის თუ არა ეს ორი ცვლადი ერთმანეთს , გამოიყენე ახლად ნასწავლი ოპერატორი != 
name1="nini"
name2="mari"
if name1 != name2:
    print("ეს ორი ცვლადი არ არის ტოლი")
else:
    print("ეს ორი ცვლადი ტოლია")






