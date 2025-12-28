# loop in python.

i = 1
while i <= 100:                       # also called stoping condition.
    print("hello world" , i)
    i += 1

i = 1
while i <= 100:
    print(i)
    i += 1

nums = (1,4,9,16,25,36,49,64,81,100)

x = 36

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("ELEMENT FOUND AT IDX", i)
        
    else:
        ("finding..")
    i += 1

# ________________________________________________________________________
# for loop.

nums = [1, 2, 3, 4, 5]

for val in nums:
    print(val)

# _________________________________________________________________________
vagies = ["carrot", "ladyfinger", "tamato", "onion", "loky", "bringle"]

for val in vagies:
    print(val)

# ___range__________________________________________________________________


for i in range(10):               # range (stop).
    print(i)


for i in range(2, 10):            # range  (start and stop).
    print(i)


for i in range(2, 10, 2):         # range   (start , stop and step).
    print(i)

n = int(input("enter some value: "))

for i in range(1, 11):
    print(i * n)


# ________pass_statement____________________

for i in range(5):
    pass

print("hello world")

 