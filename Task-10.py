org_list=[1,2,3,4,5,6,7,8,9,10]
i=0
extracted_list=[]
while i<5:
    element=org_list[i]
    extracted_list.append(element)
    i+=1
print("Extracted list is: ",extracted_list)
reverse_list=[]
for i in extracted_list:
    new_elements=extracted_list[5-i]
    reverse_list.append(new_elements)
print("Reverse list is : ",reverse_list)