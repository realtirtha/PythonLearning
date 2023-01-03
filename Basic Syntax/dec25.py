

print("Ajita")

x=5
print(type(x))

a="5"
b="4"
c=a+b
print(c)


a=5
b=4
c=a+b
print(c)

letter="A"
if letter=="B":
    print("letter is B")
elif letter=="C":
    print("letter is C")
elif letter=="A":
    print("letter is A")
else:
     print("letter isnot A,B or c")

count=0
while(count<3):
         count=count+1
         print("Hello World")

n=4
for i in range(0,n):
         print(i)

for i in range(1,5):
    for j in range(i):
        print(i,end='')
    print()
'''
try:
 print(x)
except:
 print("An exception occurred")


name=input("What is your name?")

d="Hello"
a=(input("enter first name"))
b=(input("enter last name"))
print(d,b,a) 


#sum of iteration
print("print current and preious number and their sum in range(10)")
previousNum=0
for i in range(1,11):
    sum1=previousNum+i
    print("current Number",i,"previous number",previousNum,"sum:",sum1)
    previousNum=1
    #functions
def greetings():
    print('Hello World!')
    greetings()
    print("printing outside of a function")
    #function with two arguments
def add_numbers(num1,num2):
    sum=num1+num2
    print('sum:',sum)
add_numbers(2,4)
#function definition
def find_square(num):
    result=num*num
    return result
    square=find_square(3)
    print('square:',square)
    #function definition
def get_square(num):
    return num*num
for i in[1,2,3]:
            #function call
        result=get_square(i)
        print('square of',i,'=',result)
        #prgm to find sum of multiple numbers
def find_sum(*numbers):
    result=0
    for num in numbers:
     result=result+num
    print("sum= ",result)
#function call with 3 argments
find_sum(1,2,3)
#function call with 2 arguments
find_sum(4,9)
#def my_function(*fruits):
print("The selected fruit is"+fruits[1])
def intro(**data):
    print("\nData type of argument:",type(data))
    for key,value in data.items():
     print("{} is {}".format(key,value))
intro(firstname="sita",Lastname="Sharma",Age=12,phone=1234567890)

intro(firstname="Ajita",Lastname="Gyawali",Email="jnawaliajita@gmail.com",Country="Nepal",Age=20,phone=9812334567)

'''