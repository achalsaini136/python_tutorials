f = open('demo.txt', 'r')
data = f.read()
print(data)
print(type(data))
f.close()

# ______________________________________
f = open('demo.txt', 'r')

data = f.read(5)
print(data)

f.close()

# ______________________________________
f = open('demo.txt', 'r')

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()

# ______________________________________

f = open('demo.txt', 'r')

data = f.read()
print(data)

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()


# ______________________________________
f = open('demo.txt', 'w')

f.write('i will start learning html and css after ')

f.close()

# ______________________________________

f = open('practice.txt', 'w')       # creating folder.
f.close()


f = open('samole.txt', 'a')         # creating folder
f.close()


# _________________________________________
# rough__

f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()


# _______________________________________________
# how to overwrite.____

f = open("demo.txt", "w")
data = f.write('my name is achal. i want to be a python developer.')
f.close()

f = open("demo.txt", "r")

data = f.read()
print(data)

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

line3 = f.readline()
print(line3)

f.close()

f = open('demo.txt', 'a')
data = f.write('my brother name is amit and.\n my second brother name is manish \n')
f.close()


f = open('sample.txt', 'x')
data = f.write('is this really you')
f.close()
# ___________________________________________________________________________________________
f = open('sample.txt', '+')
data = f.write('i am learning japnease.\n i want to go japan. \n i want to live in japan')
f.close()





f = open('demo1.txt', 'r+')
data = f.write('is this really a sample file or anything else')
f.close()


f = open('sample.txt', 'r+')
data = f.write('achal')
print(f.read())
f.close()


f = open('sample.txt', 'w+')                     # if we use w+ the file will trunkcate and all the data will disappear and we can write it from sart.
print(f.read())
data = f.write('my name is achal saini')
f.close()


f = open('sample.txt', 'a+')                      # just like append mode and pointer is at the end of the sentence.
print(f.read())
data = f.write('\n i want to go in japan. \n and i want to live a pecefull life in japan') 
f.close()



# with syntax_____________________
 

with open('sample.txt', 'a') as f:
    data = f.write('\nmy dream is to travel the world and experience travelling .')
    print(data)


# deleating a file ______________________-

import os
os.remove('sample.txt')

# practice question_______________++

# creat a new file 'practice.txt' using python. add the followig data in it.
#             Hi everyone
#             we are learning file i/o
#             using java
#             i like programing in java
# answer_

f = open('practice.txt', 'w')
data = f.write('Hi everyone.\nwe are learning file i/o.\nusing java.\ni like programing in java')
f.close

# write a function that replace all the occurance of 'java' with 'python' in above file

# first method but long   wrong.___________________________________________________________
 
f = open('practice.txt', 'r+')
line1 = f.write('Hi everyone\n')
print(line1)

line2 = f.write('we are learning file i/o\m\n')
print(line2)

line3 = f.write('using python\n')
print(line3)

line4 = f.write('i like programing in python\n')
print(line4)

f.close()


# second method____  right_____________

with open('practice.txt', 'r+') as f:
    data = f.read()

new_data = data.replace('java','python')
print(new_data)

with open('practice.txt', 'w') as f:
    f.write(new_data)

 



# search if the word 'learning' exists in the file or not.____


# by myself___

with open('practice.txt', 'r') as f:
    data = f.read()

new_data = data.find('learning')
print(new_data)

with open('practice.txt', 'r') as f:
    f.read(new_data)
    
# by youtube__

word = ('learning')
with open('practice.txt','r') as f:
    data = f.read()
    if(data.find(word) != -1):
        print('found')

    else:
        ('not found')


# by using function.______

def check_for_word():
    word = ('learning')
    with open('practice.txt','r') as f:
        data = f.read()
        if(data.find(word) != -1):
            print('found')

        else:
            print('not found') 

check_for_word()

# write a function to find in which line of the file does the word 'learning' occur first.
# print  -1 if word not found.

 
def check_for_line():
    word = ('learning')
    data = True
    line_no = 1

    with open('practice.txt', 'r') as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1


check_for_line()



def check_for_line():
    word = ('programing')
    data = True
    line_no = 1

    with open('practice.txt', 'r') as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1 

    return -1     


check_for_line()




def check_for_line():
    word = ('java')
    data = True
    line_no = 1

    with open('practice.txt', 'r') as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

        else:
            print(-1)

check_for_line()




# from a file contaning numbers seperated by comma, print the count of even numbers.
 
with open('numbers.txt', 'r') as f:
    data = f.read()
    print(data)
 

# __ first method.

nums = "" 
for i in range(len(data)):
    if(data[i] == ","):
        print(nums)
        nums = "" 

    else:
        nums += data[i]

       

# __ second method.

count = 0
with open('numbers.txt', 'r') as f:
    data = f.read()
    print(data)

nums = data.split(",")
for val in nums:
    if(int(val) % 2 == 0):
        print(nums)
        count += 1

print(count)

