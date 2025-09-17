d1={"Yash":"98" , "Shristi":"99" , "Amit":"92"}
name=input("Enter the name to display his/her marks: ")
if name in d1.keys():
    print(name, "marks is",d1.get(name))
else:
    print("student not found")