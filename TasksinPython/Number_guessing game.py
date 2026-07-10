num=int(input("Enter any number:"))
your_num=int(input("Enter your number:"))
count=1
while True:
    if num>your_num:
        print("Too high");
    elif your_num==num:
        print("Number founded")
        break
    else:
        print("Too low")
    your_num=int(input("Enter your number:"))
    count=count+1
print("Attempts:",count)