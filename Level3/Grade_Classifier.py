score=int(input("Enter the score:"))
if score>=90:
    print("Grade:A")
    print("Pass")
elif (score>=80) and (score<90):
    print("Grade:B")
    print("Pass")
elif (score>=70) and (score<80):
    print("Grade:C")
    print("Pass")
elif (score>=60) and (score<70):
    print("Grade:D")
    print("Pass")
else:
    print("Grade:F")
    print("Fail")