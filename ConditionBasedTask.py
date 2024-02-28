
# to find the given number is -ve/+ve/0
num = float(input("Enter a number: "))
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")

#To find even or odd
num1 = float(input("Enter a number: "))
if num1%2==0:
    print("even")
else:
    print("odd")

#
Sub1 = float(input("Enter a number: "))
Sub2 = float(input("Enter a number: "))
Sub3 = float(input("Enter a number: "))
marks = (Sub1+Sub2+Sub3)/3
if marks > 75:
    print("Grade A")
elif marks < 75 and marks>65:
    print("Grade B")
elif marks == 65 and marks < 65:
    print("Grade C")
else:
    print("failed")

