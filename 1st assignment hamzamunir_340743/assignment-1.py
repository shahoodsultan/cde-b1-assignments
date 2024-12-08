# 1.Print Your Name with your Father name and Date of birth using suitable escape sequence charactor
print("Name:\tM Owais Hasan Khan")
print("Father Name:\tPervez Hasan Khan")
print("DOB:\t25-October-2002")

# Write your small bio using variables and print it using print function
name="Owais"
age=21
f_name="Pervez Hasan Khan"
edu="BSCS"
print("------BIO-----")
print(name)
print(age)
print(f_name)
print(edu)

# 2.Write a program in which use all the operators we can use in Python
a=10
b=18

c=a+b
print(c)
c=a-b
print(c)
c=a/b
print(c)
c=a%b
print(c)
c=a*b
print(c)

"""3.Completes the following steps of small task:
Mention Marks of English , Islamiat and Maths out of 100 in 3 different variables
Mention Variable of Total Marks and assign 300 to it
Calculate Percentage"""

eng=78
isl=88
math=94

per=(78+88+94)/300*100
print(per)

# 4.A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.
sal=int(input("Enter Your Salary:"))
ser=int(input("Enter Your Year Of Ecperience:"))
if ser>=5:
    bonus=sal*0.05
    print("Congartulatios Your Salary After Bonus Is:",bonus)
else:
    print("You Are Not Eligible For Bonus")

# 5.Write a program to check whether a person is eligible for voting or not. (accept age from user) if age is greater than 17 eligible otherwise not eligible

age=input("Enter Your Age:")
if age>=18:
    print("You Are Eligible For Vote")
else:
    print("Sorry You Are Not Eligible For Voting")

# 6.Write a program to check whether a number entered by user is even or odd.
num=int(input("Enter The Number:"))
if (num%2==0):
    print("TheNumber IS Even")
else:
    print("The Number Is Odd")

# 7.Write a program to check whether a number is divisible by 7 or not. Show Answer
num=int(input("Enter The Number:"))
if (num%7==0):
    print("TheNumber Is Divisible By 7")
else:
    print("The Number Is Not Divisible By 7")

# 8.Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise print "Bye".
num=int(input("Enter The Number:"))
if (num%5==0):
    print("Hello")
else:
    print("Bye")

# 9.Write a program to display the last digit of a number.
# 10.Take values of length and breadth of a rectangle from user and print if it is square or rectangle.

len=int(input("Enter The Length:"))
breadth=int(input("Enter The Breadth:"))

if (len==breadth):
    print("It Is Square")
else:
    print("Rectangle")

# 11.Take two int values from user and print greatest among them.

a=int(input("Enter The Fisrt Value:"))
b=int(input("Enter The Second Value:"))

if(a>b):
    print("The Greatest Value Is:",a)
elif(b>a):
    print("The Greatest Value Is:",b)
else:
    print("Not Valid")

# 12.A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.

quan=int(input("Enter Quantity"))
if(quan>1000):
    dis=quan*0.10
    print("Your Discount Is:",dis)
    tot=quan-dis
    print("Total Cost After Discount is:",tot)
else:
    print("You Are Not Eligible For Discount")

"""13.A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade."""

marks = int(input("Enter your marks (out of 100): "))
if marks < 25:
    grade = "F"
elif 25 <= marks < 45:
    grade = "E"
elif 45 <= marks < 50:
    grade = "D"
elif 50 <= marks < 60:
    grade = "C"
elif 60 <= marks < 80:
    grade = "B"
else:
    grade = "A"

print(f"Your grade is:",grade)

"""14. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not."""

classes_held = int(input("Enter the total number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))
attendance_percentage = (classes_attended / classes_held) * 100

print("Percentage of classes attended:",attendance_percentage)

if attendance_percentage >= 75:
    print("The student is allowed to sit in the exam.")
else:
    print("The student is NOT allowed to sit in the exam.")

 # 15.Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.
 
classes_held = int(input("Enter the total number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))
attendance_percentage = (classes_attended / classes_held) * 100


print("Percentage of classes attended:",attendance_percentage)
if attendance_percentage >= 75:
    print("The student is allowed to sit in the exam.")
else:
    medical_cause = input("Does the student have a medical cause? (Y/N): ")
    if medical_cause == 'Y':
        print("The student is allowed to sit in the exam due to a medical cause.")
    else:
        print("The student is NOT allowed to")

# 16.Write a program to check if a year is leap year or not.

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year," is not a leap year.")

"""17.  Ask user to enter age, gender ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
if employee is female, then she will work only in urban areas.
if employee is a male and age is in between 20 to 40 then he may work in anywhere
if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
And any other input of age should print "ERROR"""

age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
marital_status = input("Enter your marital status (Y/N): ")

if gender == 'F':
    print("The employee will work in urban areas only.")
elif gender == 'M':
    if 20 <= age <= 40:
        print("The employee may work anywhere.")
    elif 40 < age <= 60:
        print("The employee will work in urban areas only.")
    else:
        print("ERROR")
else:
    print("ERROR")

"""18.Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria : Unit Price
uptp 100 units no charge Next 200 units Rs 5 per unit After 200 units Rs 10 per unit (For example if input unit is 350 than total bill amount is Rs.3500 (For example if input unit is 97 than total bill amount is Rs.0 (For example if input unit is 150 than total bill amount is Rs.750"""
units = int(input("Enter the number of units consumed: "))
bill_amount = 0

if units <= 100:
    bill_amount = 0
elif 101 <= units <= 300:
    bill_amount = (units - 100) * 5
else:
    bill_amount = (200 * 5) + (units - 300) * 10

print("Total bill amount is Rs",bill_amount)

# 19.Take input of age of 3 people by user and determine oldest and youngest among them.
age1=int(input('enter age1: '))
age2=int(input('enter age2: '))
age3=int(input('enter age3: '))
if age1>age2 and age1>age3:
    print('age1 is oldest')
elif age2>age1 and age2>age3:
    print('age2 is oldest')
else:
    print('age3 is oldest')
if age1<age2 and age1<age3:
    print('age1 is youngest')
elif age2<age1 and age2<age3:
    print('age2 is youngest')
else:
     print('age3 is youngest')




