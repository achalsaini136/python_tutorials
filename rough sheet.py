# while loop.

count = 1

while count <= 5:
    print('apnacollage')
    count += 1

    print(count)


i = 1

while i <= 10:
    print('hello world')
    i += 1

i = 0

# while i <= 100:
#     print(i)
#     i += 2

i = -100

while i <= -1:
    print(i)
    i += 5

    print('count')


i = 1

while i <= 10:
    print('hello world', i)
    i += 1

i = 100

while i >= 1:
    print(i)
    i -= 1 


i = 100

while i >= 1:
    print(i)
    i -= 1 


i = 1
while i <= 100:
    print(i)
    i += 1

i = 100

while i >= 1:
    print(i)
    i -= 1


n = int(input("enter some value: "))

i = 1

while i <= 10:
    print(i * n)
    i += 1


value = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

i = 1

while i <= 10:
    print(i ** value)
    i += 1

i = 1

while i <= 10:
    print(4 * i)
    i += 1

# print the element of the following list by ising while loop.
        # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

i = 1

while i <= 10:
    print(i ** 2)
    i += 1


nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0

while idx < len(nums):
    print(nums[idx])
    idx += 1

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36
i = 0

while i < len(nums):
    if(nums[i] == x):
        print('found at idx', i)
    else:
        print('finding')
    i += 1    


insect = ['spider', 'cockroch', 'lion', 'tiger', 'bear']

i = 0

while i < len(insect):
    print(insect[i])
    i += 1

val = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for i in val:
    print(i)


val = ['tiger', 'cat', 'lion', 'dog', 'elephant', 'crow', 'fish', 'snake']
i = 0
while i < len(val):
    print(val[i])
    i += 1



nums = ['cat', 'tiger', 'lion', 'elephant']

i = 0 

while i < len(nums):
    print(nums[i])
    i += 1


str = "hello world"

for char in str:
    print(char)


i = 0
while i <= 10:
    if(i%2 != 0):
        i += 1
        continue
    print(i)
    i += 1


i = 1
while i <= 10:
    print(i)
    if(i == 3):
        break
    i += 1

    #  print("compleate..")


i = 0

while i <= 10:
    if(i == 3):
        print(i)
        i += 1
        continue
    else:
        print('finding')
    i += 1


i = 0

while i <= 10:
    print(i)
    if(i == 4):
        break
    i += 1

print('compleate')   



str = 'hello world'

for char in str:
    if(char == 'o'):
        print('value found')
    print(char)
else:
    print('finding')

print('loop end')



# ______question_____________________

# print the element of the following list usung loop.
#   [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for i in nums:
    print(i)
    

# search for a number x in this tuple using loop.
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

page =  (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36

for i in page:
    if(i == x):
        print('found')
        break
    print(i)
else:
    print('compleate.')

print('loop end') 



page =  (1, 4, 9, 16, 25, 36, 49, 36, 64, 81, 100, 36)

x = 36

for i in page:
    if(i == x):
        print('found')
    print(i)
else:
    print('compleate.')

print('loop end') 

# _________________________________________________________________________________________________________________________________
# __________________incompleate_________


nums =  (1, 4, 9, 16, 25, 36, 49, 36, 64, 81, 100, 36)

x = 49

idx = 0
                                                                    # wrong , wrong , wrong
for el in nums:
    if(idx == x):                                            # mistake idx ki jagha el lagana tha
        print('found at idx', idx)
    idx += 1

# ______________________________________________________________________________________________________________________

nums =  (1, 4, 9, 16, 25, 36, 49, 36, 64, 81, 100, 36)

i = 0

x = 36

while i < 10:
    print(i)
    i += 1
    if(nums[i] == x):
        print('found at idx')
        i += 1
else:
    print('finding')

print('loop end')


nums =  (1, 4, 9, 16, 25, 36, 49, 36, 64, 81, 100, 36)

x = 36

idx = 0

for el in nums:
    if(el == x):
        print('found at idx', idx)
        idx += 1
        break
    print(el)
    idx += 1
else:
    print('finding..')

print('loop end..')

# ________________________________________________________________________________________________
nums =  (1, 4, 9, 16, 25, 36, 49, 36, 64, 81, 100, 36)

x = 36

idx = 0
for el in nums:
    if(el == x):
        print('found at idx', idx)
    idx += 1



seq = range(5)

for i in seq:
    print(i)



for i in range(5):
    print(i)

for i in range(1, 5):
    print(i)

for i in range(2, 5, 1):
    print(i)

nums =  (1, 4, 9, 16, 25, 36, 49, 36, 64, 81, 100, 36)

i = 0

while i < len(nums):
    print(nums[i])
    i += 1

for i in range(1, 100):
    print(i)

for i in range(100, 0, -1):
    print(i)

n = int(input('enter value:'))

for i in range(1, 11):
    print(i * n)

n = 5

i = 1

sum = 0

while i <= n:
    sum += i
    i += 1

print('total sum', sum)


n = int(input('enter value: '))

fact = 1

for i in range(1, n+1):
    fact *= i

print('factorial', fact)



 