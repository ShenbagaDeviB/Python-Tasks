my_dictionary={"name":"Shen",
               "age":20,
               "grade":"B",
               "subject":"IOT"}
for x,y in my_dictionary.items():
    print(f"The student {x} is {y}")
my_dictionary.update({"grade":"A"})
my_dictionary["passed"]="true"
print(my_dictionary)