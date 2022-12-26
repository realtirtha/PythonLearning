#python3 program for explaining the use of list, tuple, set and and dictionary

#languages: list of dictionaries

languages = [
    {"Python": "machine learning", "R":"Machine learning"},
    {"python": "web development", "java script": "web development", "HTML": "web development"},
    {"c++": "game development","python": "game development"},
    {"java": "app development", "kotlin": "app development"} 
]

print(*[key for i in languages for key in i.keys()],sep = "\n")

'''
#item price in dollars
oldPrice= {'milk':1.02,'coffee':2.5,'bread':2.5}
dollarToPound= 0.76
newPrice = {item: value*dollarToPound for (item, value) in oldPrice.items()}
print()
print(newPrice)

###
orgDict= {'tirtha': 20, 'sudeepna':23, 'ajita': 20}
evenDict= {k:v for (k,v) in orgDict.items() if v%2==0}
print(evenDict)

###
org= {'jack':38,'michael':48, 'guido': 57, 'john':33}
new={k:v for (k,v) in org.items() if v%2!=0 if v<40}
print(new)
'''

'''
#comprehension

sq_dict = dict()
for num in range(1,11):
    sq_dict[num] = num*num
print(sq_dict)

#SAME AS
square_dict = {num: num*num for num in range(1,11)}
print("compresion using if:")
print(square_dict)

print()
myDict = {x: x**2 for x in [1,2,3,4,5]}
print("creation using list compresion")
print(myDict)

newDict= {x: x**3 for x in range(10) if (x**3 % 4) == 0}
print(newDict)

'''

'''
#dictionary
d={}

#adding the key value pair
d[5] = "Five"
d[10] = "Ten"
d[11] = "Ten1"
print("Dictionary: ", d)
                    #dictionary ma value same vaye pani farak pardeina
d[10] = "Sudeepna"  # value key xei repeat hudeina
print("After : ", d) 
print(d[10]) # printing by key
print() 



l=[1,2,3,4,5]

#Tuple
t=tuple(l)

#tuples are ummutable
print("Tuple",t)
print()

t.add(10) #we cannot modify tuples data
print()
print(t)


#Lists
l=[]

#adding element to the list
l.append(5)
l.append(10)

print("adding 5 and 10 in list", l)

l.append(12)
l.append(1)
l.pop()

print(l)


#popping elements from list
l.pop()
print("popped one element form list", l)
print()



#set
s=set()

#adding element from set
s.add(5)
s.add(10)
s.add(12)
print("Adding 5 and 10 in set", s)
print()
s.remove(5)
print("removed one element from set: ", s)

'''

