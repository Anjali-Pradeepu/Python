#list operations and functions

list_elements=[10,20,30,40,50,10,20]
print(list_elements)

#No:of elements
print(len(list_elements))

#count of elements
print(list_elements.count(10))

#insert new element
list_elements.insert(1,100)
print(list_elements)

#extending the list with another list
l2=[5,10,15]
list_elements.extend(l2)
print(list_elements)

#pop function
list_elements.pop(1)    #pop from the frst position
print(list_elements)
list_elements.pop()     #pop from the end of the list
print(list_elements)

#remove function
list_elements.remove(40)  #removes data directly instead of pop(removes from the position)
print(list_elements)

#index function
print(list_elements.index(20))

#reverse function
list_elements.reverse()
print(list_elements)

#sort function
list_elements.sort()
print(list_elements)
