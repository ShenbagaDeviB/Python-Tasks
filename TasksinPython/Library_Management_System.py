'''books=["C","C++","Java","Python"]
members=["Shen","Ren","Resh"]
my_book=input("Enter your needed book:")
my_member=input("Enter the author:")
if my_book in books:
    print(my_member,"borrowed",my_book,"book.")
    print("Transaction completed successfully..")
else:
    print("Book not found!!!")'''
books={"C":100,"C++":300,"JAVA":400,"PYTHON":800}
members=["Shen","Ren","Resh"]
my_book=input("Enter your needed book(in capital):")
my_member=input("Enter the author:")
borrowed_member=input("Enter the name:")
if my_book in books and my_member in members:
    print(my_member,"borrowed",my_book,"book from",borrowed_member,"and transacted",books[my_book],"rupees")
else:
    print("Book not found!!!")   