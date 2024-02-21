thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#To insert a new item at the specified index or location
thislist.insert(2, "Orange")
print(thislist)

#Add new item at the end of the LIST
thislist.append('Apple')
print(thislist)

#Extending a list by another list
tropical = ["mango", "pineapple", "papaya"]
shailentup = ("A","B","C")
shailenset = {"a","b"}
tropical.extend(shailentup)
tropical.extend(shailenset)
print(tropical)

#removes the first occurance of the value
thislist.remove('orange')
print(thislist)

#pop removes the specified index value
thislist.pop(1) # if index not specified then it removes the last value
print(thislist)

#del removes the specified index
del thislist[3] #del thislist deletes the whole list
print(thislist)

# del thislist
# print(thislist)

# removes the values in the list but list still exists
thislist.clear()
print(thislist)


thislistnew = ["apple", "banana", "cherry"]
[print(x) for x in thislistnew]


