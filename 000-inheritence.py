"""
Present inheritence
-------------------
A class (child class or derived class) inherits properties, methods and
functions from another class (parent class or base class).
"""

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def printpersondata(self):
        print('Firstname: {}\nLastname: {}\nAge: {}\n'
              .format(self.firstname, self.lastname, self.age))

# Create a Person class object and print the data of person.
person_1 = Person('Alice', 'Smith', '36')
person_1.printpersondata()



# Create a derived class
# Using "pass" instead of __init__() is not an elegant solution
class Children(Person):
    pass

person_2 = Children('Bob', 'Riley', '7')
person_2.printpersondata()



# Create an other derived class
# Using __init__() in child class overrides the inheritence
# Get back inheritence of parent's __init__() function, must call a parent's
# __init__() function directly
class Spouse(Person):
    def __init__(self, firstname, lastname, age):
        Person.__init__(self, firstname, lastname, age)

person_3 = Spouse('Josh', 'Riley', '40')
person_3.printpersondata()



# Create an other derived class
# Add new properties
# However, using super() instead of calling parent's __init__() function
# directly is more pythonic
class Worker(Person):
    def __init__(self, firstname, lastname, age, workplace):
        super().__init__(firstname, lastname, age)
        self.workplace = workplace

    def printpersondata_2(self):
        print('Firstname: {}\nLastname: {}\nAge: {}\nWorkplace: {}\n'
              .format(self.firstname, self.lastname, self.age, self.workplace))

person_4 = Worker('Charlie', 'Matthews', '37', 'Office')
person_4.printpersondata()
person_4.printpersondata_2()