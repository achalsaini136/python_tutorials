print("achal is my name.", "my age is 19.")
print(23)
print(34 + 55)

# variable

name = "achal" 
age = 19
prise = 20.22
print("my name is : ", name )
print("my age is : ", age ) 

name = "achal"
age = 19

age2 = age

print("my age is : ", age2 )

 
# detection of data type

name = "achal"
age = 19
price = 22.23

print((type(name)) , (type(age)) , (type(price)))
 
age = 19
old = False
a = None

print((type(old)) , (type(a)))

a = 29
b = 10
sum = a + b 
print(a + b)

# arthmetic operator

a = 5
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b) # when we divide value always float
print(a % b) # return reminder
print(a ** b) # means a^b (5^2)

# ralation / comparision operator

a = 50
b = 20

print(a == b) # false
print(a != b) # true (means not equalto)
print(a >= b) # true
print(a > b) # true
print(a <= b) # false
print(a < b) # false

# assignment operators(=, +=, -=, *=, **=, %=, /=)
num = 10
num %= 10 # (num = num + 10)
print(num)

# logical operator(not, and, or) (cant understand_'not')
a = 50 
b = 30
print(not False)
print(not (a > b))

val1 = True
val2 = False
print("and operator: ", val1 and val2) # when both value are true (give true)

print("or opertator: ", val1 or val2) # either one value are true (give true)


val1 = True
val2 = False
print("or operator: ", (val1 == val2) or (val1 >= val2))

# type conversion
a = 4            # convert int into floating value (2 = 2.0)
b = 2.5
sum = a + b
print(sum)

# type casting

a = float("4")
b = 2.5
sum = a + b
print(sum)

a = 3.14
a = str("3.14")
print(type(a))

age = input("enter your age: ")
print("you enter" , age)

name = str(input("enter your name: "))
age = int(input("enter your age: "))
marks = float(input("enter your marks: "))

print("welcome master")
print("name =" , name)
print("age =" , age)
print("marks =" , marks)
print(type(age))
print(type(marks))


# two sting in a same line.

print('helloworld', end = " ")
print('helloworld')