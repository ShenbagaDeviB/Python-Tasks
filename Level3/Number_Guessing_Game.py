num=int(input("Enter the number:"))
n=int(input())
count=1
while(True):
    if num>n:
        print("Too high")
    elif num==n:
        print("Found")
        break
    else:
        print("Too low")
    n=int(input())
    count=count+1
print(count)