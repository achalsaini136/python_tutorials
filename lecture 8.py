# class and object in python.

# 1) creating class.

class Car:
    name = 'Bugatti'

# 2) creating object (instance).

car1 = Car()
print(car1.name)

car2 = Car()
print(car2.name)

 
class Student:
    def __inhit__(self,fullname):
        self.name = fullname
        print('adding new student in database..')

s1 = Student("sonu")
print(s1.name)




# these_two_are_same_type_of_constructor._____________.

# first______________________

class Student:

    def __init__(self,fullname):
        self.name = fullname
        print('adding new student in database..')

s1 = Student('karan')
print(s1) # karan

s2 = Student('sonu')
print(s2.name) # sonu




# second____________________________

class Student:
    def __init__(self,name,marks,roll,):
        self.name = name
        self.marks = marks
        self.roll = roll
        print('adding student imformation in database')

s1 = Student('karan', 80, 23,)
print(s1.name, s1.marks, s1.roll)

s2 = Student('sonu', 91, 24)
print(s2.name, s2.marks, s2.roll)




# second_type_of__constructer.___________.

#     defoult_constructor.




class Student:
    def __init__(self,name,marks,roll,):
        self.name = name
        self.marks = marks
        self.roll = roll
        print('adding student imformation in database')

s1 = Student('karan', 80, 23,)
print(s1.name, s1.marks, s1.roll)

s2 = Student('sonu', 91, 24)
print(s2.name, s2.marks, s2.roll)




# two type of constructor.___



class Student: 
                   # defoult constructor. which has only one parameter (self)
    def __init__(self):
        print('adding impformation in database')


                  # parameterized constructor. which has more than one constructor (self, name, mark, roll)
    def __init__(self,name,mark,roll):
        self.name = name
        self.mark = mark
        self.roll = roll
        print('adding new student data in database')

s1 = Student('sonu', 93, 22)
print(s1.name, s1.mark, s1.roll)




# class and instances (attribute).

class Student:
    collage_name = 'tokyo university'     # this is a class attribute.

    def __init__(self,name,mark):
        self.name = name                     # object attribute ; (when obj and class attr have same name object > then class).
        self.mark = mark      
        print('adding new student data in database')

s1 = Student('loyd', 80)
print(s1.name, s1.mark)

print(Student.collage_name)                        # we can also write (s2.collage_name)

s2 = Student('note', 79)
print(s2.name, s2.mark)

print(Student.collage_name)




class Student:
    collage_name = 'tokyo university'

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print('welcome student',self.name)

    def get_marks(self):
        return self.marks
    
s1 = Student('note', 87)
s1.welcome()
print(s1.get_marks())

 



# question___.

# create student class that take name and marks of three subject as argument in constructor. then create a method to print the average.

# first method.

class Student:
    def __init__(self, name, math, bio, eng):
        self.name = name
        self.math = math
        self.bio = bio
        self.eng = eng
        self.marks = [math, bio, eng]

    def get_avg(self):
        total = sum(self.marks)
        avg = total/3
        print('hi', self.name, 'your avg score is')

s1 = Student('name', 88, 89, 90)
print(s1.name, s1.math, s1.bio, s1.eng)
s1.get_avg() 



# second method____.

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print('hi', self.name, 'your average score is', sum/3)
        

s1 = Student('note',[88, 89, 90])
print(s1.name,s1.marks)
s1.get_average()

# _______________________________________________________________________________________________________________________________
# rough_work____________________________________________________________________________________________________________________

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def hello():
        print('hello')

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print('hi', self.name, 'your avg marks is', sum/3)

s1 = Student('note', [88, 89, 90])
s1.get_avg()
s1.hello()
 
s1.name = "zero"
s1.get_avg


# ____________________________________________________________________________________________________________________________

# static_method

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print('hello')

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print('hi', self.name, 'your avg marks is', sum/3)

s1 = Student('note', [88, 89, 90])
s1.get_avg()
s1.hello()
 
s1.name = "zero"
s1.get_avg





# abstraction.__  (all the unnesscery thing are unable to see)

class Car:
    def __init__(self):
        self.acc = False
        self.clutch = True
        self.brk = False

    def start(self):
        self.clutch = True
        self.acc = True
        print('car_started..')

car1 = Car()
car1.start()


# question._.

# create account class with 2 attrubute - balance and account no. create method for debit , credit and printing the balance.
        # first method by self.

class Account:
    def __init__(self, bal, acc):
        self.bal = bal
        self.account_no = acc

# debit method.

    def debit(self):
        val = int(input('enter amount value :'))
        self.bal -= val
        print('hi','your account balance is',self.bal)
        print('total bal', self.total_bal)

# credit method.
    
    def credit(self):
        val = int(input('enter cash : '))
        self.bal += val
        print('hi','your account balance is',self.bal)
        print('total bal', self.total_bal)
    
    def total_bal(self):
        return self.bal



acc1 = Account(10000, 123456)
acc1.debit(2468)
print('total bal')
acc1.credit(65869)
print('total bal')
acc1.total_bal()

        #  second method 

class Account:
    def __init__(self, bal, acc):
        self.bal = bal
        self.account_no = acc

# debit method.

    def debit(self, amount):
        self.bal -= amount
        print('hi',amount,'have debited')
        print('total bal =', self.get_bal())

    
# Credit method.

    def credit(self, amount):
        self.bal += amount
        print('hi', amount, 'have credited')
        print('total bal =', self.get_bal())

    def get_bal(self):
        return self.bal


acc1 = Account(10000, 123456789)
acc1.debit(3534)
acc1.credit(3982)
acc1.credit(50000)
acc1.debit(15000)
acc1.credit(4000)



# ____________________________________________________________________________________________________________________________________

# second part of oops.

class Student:
    def __init__(self,name):
        self.name = name

s1 = Student('note')
print(s1.name)
del s1.name                           # del is a delete keyword.
print(s1.name)

# ______________________________
# private attribute and methods.
                                        #    this data is public.
class Account:
    def __init__(self, account_no, account_pass):
        self.account_no = account_no
        self.account_pass = account_pass

s1 = Account("12345", "abcde")

print(s1.account_no)
print(s1.account_pass)


                                #     this data is private by using two underscore "__" we can private the data.

class Account:
    def __init__(self, account_no, account_pass):
        self.account_no = account_no
        self.__account_pass = account_pass

    def reset_pass(self):
        print(self.__account_pass)

s1 = Account("12345", "abcde")

print(s1.account_no)
print(s1.reset_pass())
print(s1.__account_pass)


# second example. of private and public attribute & method.

class Person:
    __name = "annonymous"

    def __hello(self):
        print("hello person")

    def welcome(self):
        self.__hello()


p1 = Person()
print(p1.welcome())



# inheritance example.                        # it is also an single inheritance.

class Car:
    colour = "black"
    @staticmethod
    def start():
        print('car started')

    @staticmethod
    def stop():
        print('car stopped')

class Toyotacar(Car):
    def __init__(self, name):
        self.name = name


car1 = Toyotacar('fortunere')
car2 = Toyotacar('perus')

print(car1.start())
print(car1.start())
print(car1.colour)
print(car1.name)





# multi leval inheritance.          #    (i think there is something wrong in this class i have to write it again).

class Car:
    @staticmethod
    def start():
        print('car started')

    @staticmethod
    def stop():
        print('car stopped')

class Toyotacar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortunere(Toyotacar):
    def __init__(self, type):
        self.type = type

car1 = Fortunere('toyota', 'petrol')
print(car1.brand)
print(car1.type)

# ________________________________________

# example of multi level inheritence.

class A:
    variable1 = "welcome to class a"

class B:
    variable2 = "welcome to class b"

class C(A, B):
    variable3 = "welcome to class c"

c1 = C()

print(c1.variable1)
print(c1.variable2)
print(c1.variable3)

# super method.

class car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print('car started..')

    @staticmethod
    def stop():
        print('car stopped..')

class toyotscar(car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = toyotscar('lambo', 'petrol')
print(car1.name)
print(car1.type)

# _______________________________________.
# classmethd.

class Person:
    name ='anoynomous'

    # def changename(self,name):
    #    Person.name = name                  # 1)
    #    #self.__class__.name = 'shiya'      # 2)  

    @classmethod
    def changename(cls,name):
        cls.name = name

         

p1 = Person()
p1.changename('shiya')

print(p1.name)
print(Person.name)


# __________________________________________.

# property decorator.

# first method.

class Student():
    def __init__(self,eng,math,bio):
        self.eng = eng
        self.math = math
        self.bio = bio
        self.percentage = str((self.eng + self.math + self.bio) / 3) + '%'

    def calcpercentage(self):
         self.percentage = str((self.eng + self.math + self.bio) / 3) + '%'

s1 = Student(89, 88, 90)
print(s1.percentage)
         

s1.eng = 68
print(s1.eng)
s1.calcpercentage()
print(s1.percentage)


# second method.(by using property decorator ).

class Student:
    def __init__(self,eng,math,bio):
        self.eng = eng
        self.math = math
        self.bio = bio

    @property
    def persentage(self):
        return str((self.eng + self.math + self.bio) / 3) + '%'
    

s1 = Student(89,87,88)
print(s1.persentage)
s1.eng = 68
print(s1.persentage)


# polymorphism._____________________________________.

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def show(self):
        print(self.real ,'i +', self.img,'j')

    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

    def __sub__(self,nub2):
        newReal = self.real - nub2.real
        newImg = self.img - nub2.img
        return Complex(newReal,newImg)    


c1 = Complex(4, 5)
c1.show()

c2 = Complex(-8, 10)
c2.show()

c3 = c1 +c2
print(c3.show())
 

# _____practice_question._______________________

# _define a circle class to create a circle with radious r using the constructor. define an area() method of class which calculate the area of circle. define a perimeter() method of class which allow you to calculate the perimeter of circle.

class Circle:
    def __init__(self,radious):
        self.radious = radious

    def area(self):
        return (22/7) * self.radious ** 2
    
    def perimeter(self):
        return 2 * (22/7) *self.radious 
    
c1 = Circle(21)
print(c1.area())
print(c1.perimeter())


# _define a employee class with attribute role department and salery this class also has showdetails() method. create an engineer class that inherit properties from emplyoee and has additional attribute : name and age.

class Emplyoee:
    def __init__(self,role,dept,salery):
        self.role = role
        self.dept = dept
        self.salery = salery

    def showdetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salery =", self.salery)


class Engineer(Emplyoee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super(). __init__("engineer", "it", "75,000")



E1 = Engineer('shiya', 18)
E1.showdetails()
    

# _create a class called order which store items and its price. use dunder function __gt__() to convey that: order 1 > order 2 if priceof order 1 > price of order 2.

class Order:
    def __init__(self,items,price):
        self.items = items
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price

order1 = Order("chips", 20)
order2 = Order("bingo", 10)

print(order1 < order2)
         