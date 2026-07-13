try:
    f=open("data.txt","r")
    for x in f:
        try:
            print(int(x))
        except:
            print("Found insufficient data while reading")
    f.close()
except:
    print("File not found!!!!")