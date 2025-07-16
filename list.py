
# in the list foramat use["xyz", "xz", 3,5.5] use square bracket and indexing line one word in double coot is 1 means "xyz"=0, "xz"=1, 3 =2

letter =["hello","chamm",5,6.44,"rohan"]
print(letter[0])
letter[0]= "rammmm"
print(letter[0:])


# /// use of append , use of append is add string at the last of list 
letter =["hello","chamm",5,6.44,"rohan"]
letter.append("harry")

print(letter)

# /// sort method sort the list

letter =[43,5,342,56,2,433]
# letter.sort()
print(letter)


# reverse the list
# letter.reverse()
# print(letter)

# insert in list by index no
# letter.insert( 3,9999)
# print(letter)

#  pop out
letter.pop(3)
print(letter)

# remove method

letter.remove(5) 
print(letter)
