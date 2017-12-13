#input String
Name = input("Enter Name \n")
print("Name is",Name)

#input Int
Integer_no = int(input("Enter a integer \n"))
print("Entered Integer is",Integer_no)

#input Float (if int entered will be taken as 9.0)
Float_no = float(input("Enter floating point number \n"))
print("Entered Integer is",Float_no)

#input list 
list = []
size_of_list = int(input("Enter Number of elements in list \n"))
print("Enter the list")
for i in range(size_of_list):
    item=int(input())
    list.append(item)
    
#op as array
print("The Array is") 
for i in range(size_of_list):
    print(list[i])
#op as list
print("LIST",list)



