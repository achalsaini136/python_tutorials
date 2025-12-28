number = int(input("enter number: "))

rem = number % 2

if(rem == 0):
    print("even")

else:
    print("odd")

a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if(a >= b and a >= c):
    print("first the is the largest", a)
elif(b >= c):
    print("second is the largest", b)
else:
    print("third is the largest", c)    

a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))
d = int(input("enter fourth number: "))

if(a >= b and a >= c and a >= d):
    print("first the is the largest", a)
elif(b >= c and b >= c):
    print("second is the largest", b)
elif(c >= d):
    print("third is the largest", c)
else:
    print("fourth is the largest", d)    

x = int(input("enter number: "))

if(x % 7 == 00 ):
    print("multiple")
else:
    print("not a multiple")    

name = input("enter your name: ")
age = int(input("enter your age: "))
marks = float(input("enter your marks: "))

print("welcome master")
print("name =" , name)
print("age =" , age)
print("marks =" , marks)

print((type(name)),(type(age)),(type(marks)))

# write a programe to input two no. and print their sum

one = int(input("one: "))
two = int(input("two: "))
sum = one + two
print(sum)

# write a programe to input side of square & print its area

a = int(input("side of square: "))
print(a * a) 

a = float(input("enter value1: "))
b = float(input("enter value two: "))
print("average value" ,(a + b)/2)

# write a programe to input two intiger number, a and b
#   print true if a is greater then or equal to b. if not print false

a = int(input("enter first" ))
b = int(input("enter second" ))
print(a >= b)
print(a == b)

str1 = "hello"
str2 = "world"
print(len(str1))
print(len(str2))
print(len(str1 + str2))


voice = "helloworld"
print(voice[5])

name = "achal saini"
print(name[0:11])


index = "apna collage"
print(index[:12])

str = "mango"
print(str.capitalize())

str = "i am a python developer. want to join japnease company"
print(str.find("o"))

name = "my name is achal saini"
print(len(name))

# write a programe to input user name and print its lenth

name = input("enter your name.")
print("name =" , name)
print(len(name))

# write a programe to find a occurance of '$' in string

line = "this i$ my $ign $o i can do whatever i want"
print(line.count("$"))

light = "green"

if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("wait")
elif(light == "green"):
    print("go")


x = "2"

if(x >= "3"):
    print("greater no")
elif(x >= "4"):
    print("greater no")  

else:
    print("gratest")
    


# write a programe to check the number entered by user is even or odd

x = int(input("enter the value. "))

rem = x % 2

if(rem == 0):
    print("even")
else:
    print("odd")


# write a programe to find the greatest of three number enter by user

x = int(input("enter some value "))
y = int(input("enter some value "))
z = int(input("enter some value "))

if(x >= y and x >= z):
    print("largest no is", x)
elif(y >= z):
    print("larrgest no is", y)
else:
    print("largest no is" , z)


# write a programe to check if a number is multiple of seven or not

X = int(input("enter some value: "))

if(X % 7 == 0):
    print("multiple")
else:
    print("not multiple")
 
list = [3, 4, 5]
list.append(6)
print(list)

tup = (5, 4, 7, 8, 2)
print(type(tup))
print(tup[2])
print(tup[3])
print(len(tup))


# write a prigrame to ask the user to enter name of three favourate movie and store them in list.

 
a = str(input('enter movie name: '))
b = str(input('enter movie name: '))
c = str(input('enter movie name: '))

print(a)
print(b)
print(c)

sum = [a, b, c]

print(sum)


# second method


list = [input("enter first movie name: ")]
list.append((input)('enter second movie name: '))
list.append((input)('enter third movie name: '))
print(list)

# third method

animes = []
ani1 = input('enter first anime: ')
ani2 = input('enter second anime: ')
ani3 = input('enter third anime: ')

animes.append(ani1)
animes.append(ani2)
animes.append(ani3)

print(animes)



# write a programe to check if list contain a palindrome of element (hint: use copy() method)
            # [1,2,3,2,1]             [1,"abc","abc", 1]


list1 = [1,2,3,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("NOT palendrome")


# write a programe to count a number of student with the "A" grade inthe following tuple
                    # ["c", "d", "a", "a", "b", "b", "a"]

        # store the above value in the list and sort them in "A" to "D"


tup = ("c", "d", "a", "a", "b", "b", "a")
print(type(tup))
print(tup.count('b'))


list = ["c", "d", "a", "a", "b", "b", "a"]
list.sort()
print(list)



imfo = {
    "name" : "achal saini",
    "subject" : {
        "phy" : 70,
        "chem" : 80,
        "bio" : 81
    }
}

print(list(imfo.keys()))
print(tuple(imfo.keys()))




# store the following word meaning in a python in a dictonary :

    # table : "a piece of furniture", "list of facts & figure"
    # cat : "a small animal"

dict = {
    "cat" : "a small piece",
    "table" : ("a piece of furniture", "list of fact & figure")
}

print(type(dict))
print(dict)


# you are given a list of subject for student. assume one classroom is required for 1 subject. how many student are needed by all student

                    #    "python", "java", "c++", "python", "javascript",
                            # "java", "python", "java", "c++", "c"



classroom = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"
             }
print(type(classroom))
print(len(classroom))
print(classroom)


# write a programe to enter mark of 3 subject from the user and store themin a dictonary.
    # start with an empty dictonary and add one by one


dictonary = {}

x = int(input("enter phy : "))
dictonary.update({"phy" : x})

x = int(input("enter chem : "))
dictonary.update({"chem" : x})

x = int(input("enter bio : "))
dictonary.update({"bio" : x})

print(dictonary)



# figure out a way to store 9 & 9.0 as a seperate value in the set.   (you can take help of built in data type)


# first method

value = {"9", "9.0"}
print(value)

# second method

value = {
    ("int", 9),
    ("float", 9.0)
}

print(value)

# print number from 1 to 100.

i = 1
while i <= 100:
    print(i)
    i += 1


# print number from 100 to 1.

i = 100
while i >= 1:
    print(i)
    i -= 1

# print the multiplication table of number n.

n = int(input("enter some number"))
i = 1
while i <= 10:
    print(n*i)
    i += 1


# print the element of the following list using loop
    [1,4,9,16,25,36,49,64,81,100]

nums =  [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1


list= ["iron man","super man"," bat man","thor","caption america","doctor strange"]

i = 0
while i < len(list):
    print(list[i])
    i += 1



# search for a number x in this tuple using loop.
#    (1,4,9,16,25,36,49,64,81,100)

 
nums = (1,4,9,16,25,36,49,64,81,100)

x = 36

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("element found" , i)
    else:
        print("finding..")
    i += 1



# break keyword.


i = 1
while i <= 10:
    print(i)
    if(i == 3):
        break
    i += 1

    print("compleate..")




 
nums = (1,4,9,16,25,36,49,64,81,100)

x = 36

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("element found" , i)
        print("searching compleate...")
        break
    else:
        print("finding..")
    i += 1


i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue    # continue word are used to skip line.
    print(i)
    i += 1



i = 0
while i <= 10:
    if(i%2 != 0):
        i += 1
        continue
    print(i)
    i += 1




nums = [1, 2, 3, 4, 5]

for val in nums:
    print(val)
 


str = "achal", "manish", "amit", "mukul", "sonu"

for val in str:
    print(val)

str = "achal saini"

for char in str:
    print(char)


# ________________________________________________________________________
str = "apnacollage"

for char in str:
    if(char == 'o'):
        print("found o")
        break
    print(char)
else:
    print("loop end")


# ___question__________________________________________

# print the element of the following list using a loop.
        #  [1,4,9,16,25,36,49,64,81,100]

list = [1,4,9,16,25,36,49,64,81,100]

for val in list:
    print(val)


# __ second__method_____________________


nums =  [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1


# search for number x in this tuple using a loop.
    #   (1,4,9,16,25,36,49,64,81,100)

tup = (1, 4, 9, 49, 16, 25, 36, 49, 64, 81, 100, 49)                # this method are also called linear search.
x = 49

idx = 0
for val in tup:
    if(val == x):
        print("number found at idx", idx)
        break
    idx += 1

# ____range loop________________________________________

seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])


seq = range(5)

for i in seq:
    print(i)
                                        #   thease both patter are same.

for i in range(100):
    print(i)


for i in range(1, 10, 2):
    print(i)                     # (all are odd number)

for i in range(2, 10, 2):
   print(i)                      # ( all are even number)


# ____question by using for and range________________________

# print number from 1 to 100.

for i in range(101):
    print(i)

# print number from 100 to 1.

for i in range(100, 0, -1):
    print(i)

# print the multipliction table of a number n.

n1 = int(input("enter thhe value: "))
n2 = int(input("enter thhe value: "))
n3 = int(input("enter thhe value: "))

for i in range(n1, n2, n3):
    print(i)

# second method.

n = int(input("enter some value: "))

for i in range(1, 11):
    print(i * n)


# ___question___________________

# write a programe to find the sum of first n number. (using while)

n = 5

sum = 0
for i in range(1, n+1):
    sum += i


    print("total sum =", sum )


# by using while loop.

n = 7

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

    print("total sum = ", sum)


# write a programe to find the factorial of first n numbers. (using for)


n = 5

fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

    print("factorial = ", fact)

# by using for.

n = 5

fact = 1

for i in range(1, n+1):
    fact *= i

    print("factorial = ", fact)