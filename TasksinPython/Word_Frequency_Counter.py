a=input("Enter the sentence:")
a=a.lower()
a=a.split()
dict={}
for word in a:
    if word in dict:
        dict[word]+=1
    else:
        dict[word]=1
for word,count in dict.items():
    print(word,":",count)