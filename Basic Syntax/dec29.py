#dec 29

class Library:
    def __init__ (self, books):
        self.books = books

    def list_books(self):
        print("available books: ")
        for book in self.books:
            print(book)
            print()

    def borrow_book(self,borrow_book):
        if borrow_book in self.books:
            print("Get your book now")
            self.books.remove(borrow_book)
        else:
            print("Book not available")

    def receive_book(self,receive_book):
        print("You have returned the book")
        self.books.append(receive_book)

books = ['C','C++','Java']
o = Library(books)

msg = """
1. Display Book
2. Borrow Book
3. Return Book
"""

while True:
    print(msg)
    choice = int(input("Enter your choice: "))
    if choice ==1:
        o.list_books()
    elif choice ==2:
        book = input("Enter name to borrow: ")
        o.borrow_book(book)
    elif choice ==3:
        book = input("Enter book name to return: ")
        o.receive_book(book)
    else:
        print("Thank you come again")
        quit()

'''
class Person:
    def __init__(self):
        self.name = "jack mate"
    def bio(self):
        self.addr = "Bakers street, London."
        self.taxInfo = "HUAPK29971"
        self.contact = "01-777-523-342"
        print(self.addr,self.taxInfo,self.contact)
    def interest(self):
        self.favFood = "Chinese,"
        self.hobbies = "Python programming,"
        self.bloodGroup = "A+"
        print(self.favFood, self.hobbies, self.bloodGroup)

obj = Person()
print(obj.name)
obj.bio()
obj.interest()

'''

'''
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")
    def make_sound(self):
        print("meow")
class Dog:
    def __init__ (self, name, age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")
    def make_sound(self):
        print("Bark")

cat1= Cat("kitty",3)
dog1= Dog("Fluffy",4)

for animal in (cat1,dog1):
    animal.make_sound()
    animal.info()

'''
