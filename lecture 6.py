# function defination.

def calc_sum(a, b):          # a or b called parameter.
    sum = a + b
    print(sum)
    return(sum)

calc_sum(4, 5)           # known as function call.
calc_sum(19, 30)
calc_sum(21, 33)

# second___

def fun_name(a, b):
    return a + b

sum = fun_name(3, 5)              # function call.
print(sum)

sum = fun_name(44, 29)             # 44 , 29 no are called argument.
print(sum)


def print_hello():
    print('hello')

print_hello()    


def print_hello():
    print('hello')

output = print_hello()
print(output)



# first metod

def fun_avg(a, b, c):
    avg = a/3 + b/3+ c/3
    print(avg)
    return(avg)


fun_avg(98, 95, 97)

# second method

def fun_avg(a, b, c):
    sum = a + b + c
    avg = sum/3
    print(avg)
    retureturnrn(avg)


fun_avg(98, 95, 97)


# default argument__example

def func_call(a=4, b=4):
    print(a * b)
    (a * b)

func_call()


# ____question___by___self_______

# write a programe to print the length of a list(list in parameter).

def func_call(helloworld):
    print(len('helloworld'))
    return(len('helloworld'))

func_call('helloworld')

def print_helloworld():
    print(len('helloworld'))

print_helloworld()

# write a programe to print the element of list in a single line. (list in paramerer).

element = [12, 34, 56, 78, 90, 13, 24, 46, 68, 80]

def list_call(element):
    print(element)
    return(element)

list_call(element)


# ___question____by____mam_________

# write a programe to print the length of a list(list in parameter).

countary = ['india', 'japan', 'america', 'koroa', 'china', 'youkerane', 'france', 'london']
character = ['jinwoo', 'aliya', 'zero', 'miyamora', 'shikimori',]

def fun_call(list):
    print(len(list))
    return(len(list))

fun_call(countary)
fun_call(character)

hero = ['ironman', 'deadpool', 'thor', 'hulk']

fun_call(hero)

# write a programe to print the element of list in a single line. (list in paramerer).

countary = ['india', 'japan', 'america', 'koroa', 'china', 'yukarene', 'france', 'london']
 
print(countary[0], end = " ")
print(countary[1], end = " ")
print(countary[2], end = " ")
print(countary[3], end = " ")
print(countary[4], end = " ")
print(countary[5], end = " ")

def func_call(list):
    for item in list:
        print(item, end=" ")

func_call(countary)


# write a function to find the factorial of n. (n is parameter).

n = 5
fact = 1

for i in range(1, n+1):
    fact *= i
    print(fact)

def fact_call(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

fact_call(5)

# write a function to convert USD to INR.

def converter(US_doll):
    INR = US_doll * 88
    print(US_doll, "INR = ", INR , "US_doll")

converter(100)

def val_call(n):
    if(n%2 == 0):
        print('even')
    else:
        print('odd')

val_call(3)

# ______recursive_____function_______________inportant__and__same__as__loop__.


def show(n):
    if(n == -3):     # we can write any value in the place of -3.
        return
    print(n)
    show(n-1)

show(5)


def show(n):
    if(n == 0):
        return
    print(n)
    show(n - 1)
    print('loop end')


show(9)

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n

print(fact(5))


# write a recursive function to calculate the sum of first n natural number.


def call(n):
    if(n == 0):
        return 0
    return call(n-1) + n


print(call(4))


# write a recursive function to print all the the element in list.  hint. use list & index as paremeter.


anime = ['horimiya', 'mob cyco', 'that time', 'aliya something', 'angel next']


def print_list(list, idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx + 1)


print_list(anime)

