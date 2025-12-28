str1 = "achal"
len1 = (len(str1))
print(len1)

str2 = "saini"
len2 = (len(str2))
print(len2)

final_str = (str1 + str2)
final_len = (len(str1 + str2))

print(final_len)

# indexing
str = "apnna collage"
print(str[6])


# slicing
str = "apna collage"
print(str[1:4])

str = " I am studying python from youtube"
print(str.endswith("you"))

str = "i am studying python from youtube"
print(str.capitalize())
print(str)

str = "I am studying python from youtube"
print(str.replace ("youtube","nehru collage"))

str1 = "I am studying python from youtube"
print(str.find("python"))

str1 = "I am studying python from youtube"
print(str.conut("o"))
 
name = input("enter your name :")
print("length of your name" , len(name))

str = "I $am the $ sign $99.99"
print(str.count("$"))
 

age = 20  

if(age >= 18):
    print("can vote & apply for licence")
    print("and drive")

light = "pink"

if(light == "yellow"):
        print("look")
elif(light == "green"):
        print("go")
elif(light == "red"):
        print("stop")
else:
    print("light is broken")        

age = 18

if(age >= 20):
    print("can vote")
else:
    print("CANNOT vote")   

marks = 74

if(marks >= 90):
    print("grade A")
elif(marks >= 80 and marks < 90):
    print("grade B")
elif(marks >= 70 and marks < 80):
    print("grade C")


marks = int(input ("enter student mark: "))

if(marks >= 90):
    print("grade A")
elif(marks >= 80 and marks < 90):
    print("grade B")
elif(marks >= 70 and marks < 80):
    print("grade C")
                        
# nesting

age = 90
if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    print("can drive")
else:
    print("cannot drive")