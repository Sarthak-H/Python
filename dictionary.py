
#  1) its mutable ,value can change 
#  2) cannot contain duplicate key
#  3) it is unorder pair


# mydic={'name':'sarthak','marks':23,'city':'pune','roll':23}

# print(mydic)

# insert
# mydic['hello']=34
# print(mydic)

# update
# mydic.update( {'marks':11})
# print(mydic)

# reverse
# dic= dict(reversed(list(mydic.items())))
# print(dic)

# pop function 

# mydic.pop('name')
# print(mydic)

# only keys
# print(mydic.keys())

# mydics=input("enter the element ")
# print(mydic[mydics])


dic={}
name=input("enter the name")
lang=input("enter the lang")
dic.update({name:lang})
print(dic)