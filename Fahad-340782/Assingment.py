#Print Your Name with your Father name and Date of birth using suitable escape sequence charactor
print("My Name is Fahad Mehmood Alam khan and Date of Birth id 23-11-1999")

#Write your small bio using variables and print it using print function
bio="My Name is Fahad & I study in Federal Urdu universit"
print(bio)
#Add
a=1
b=2
c=a+b
print(c)
#Sub
e=3
t=6
u=e-t
print(u)
#Multiply
p=6
o=7
w=p*7
print(w)
# Division
b=5
n=1
y=b/n
print(y)
# Completes the following steps of small task:
# Mention Marks of English , Islamiat and Maths out of 100 in 3 different variables
# Mention Variable of Total Marks and assign 300 to it
# Calculate Percentage
English = 60
Islamiat =70
Math =80
total=300
optain =English+Islamiat+Math
percentage= optain/total*100
print (percentage)
 #A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

servic =int(input("Enter your service"))
if servic >5:
    salary= int(input("Einter your salary") )
    bonus=  salary*(5/100)
    print(bonus)
else:
    print("You Are Not eligable")
#Write a program to check whether a person is eligible for voting or not. (accept age from user) if age is greater than 17 eligible otherwise not eligible

age = int(input("inter your age"))
if age >17:
    print("vote")
else:
    print("you are not eligable")    

#Write a program to check whether a number entered by user is even or odd

number=int(input("Enter you number"))

print("Even" if number % 2 == 0 else "Odd")   
    

