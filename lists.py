#Creating a List

list1 = [ "r" , "a" , "j" , "a" , "t" ]
list2 = [1,2,3,4,5]
list3 = [1 , "a" , 3 , "j", 3]

#Accessing values in a List

print("Printing the whole list1 ==>", list1)
print("Printing element 2 of list 3 ==>" , list3[1])
print("Printing the 1 element from the right of list 2 ==>", list2[-1])
print("Printint all the elements except 1st of list 1 ==>" , list1[1:])
print("Printing the middle 3 values of list 2 ==> " , list2[1:4])


#Updating List elements

print("Value at list1[2] is ==> " , list1[2])
list1[2]= "newvalue"
print("New Value at list1[2] is ==> " , list1[2])

#Deleting List elements

print("The elements of list2 are ==> " , list2)
del list2[2]		#deleting the 3rd element of list 2 using 'del' keyword
print("Now the elements of list2 are ==>" , list2)
print("The new value at list2[2] is ==>" , list2[2])


#Basic List Operations

print("Length of list1 is ==> " , len(list1))
print("Let's concatenate list1 and list2 ==>", list1+list2) #Conctenation is performed using '+' operator
P = ['5']
print("Let's perform repetition operation on P", P * 5)
print("Let's check membership operation on 3 in list2==>" , 3 in list2 );
print("");

#Built-in functions in LISTS

T = [ 2,4,6,7,9,4]

print("The total length of list elements using len method == >" , len(T))
print("The max element of the list elements using max method == >" , max(T))
print("the min element of the list elements using min method == >", min(T))

tuple = ( 2 , 4 , 6 )
s = "Rajatshram"
print("We have a tuple T ==>" , tuple)
lista = list(tuple);
listb = list(s);
print("Converting a tuple into list == > " , lista)
print("Converting a string into list == > " , listb)







