marks = [90.2, 80.4, 78.6, 70.4, 66.9]
print(marks)
print(type(marks))
print(marks[3])

student = ["arjun", 80.5, 19, "japan"]
print(student[0])
student[0] = ("amit")
print(student)

student = ["arjun", 80.5, 19, "japan"]
print(student[-1:-5])

# tuple.

tup = (3, 5, 4, 9, 2, 1)
print(type(tup))
print(tup[1])
print(tup[4])
print(len(tup))

# single type tuple corret method.

tup = (4,)           # coma is necessary other wise pyhon thought it as a integer not a touple
print(type(tup))
print(tup)

# [note_=_slising_will_be_occur_same_as_list_and_string]

tup = (2, 3, 6, 7, 2, 5)
print(tup.index(6))


tup = (2, 3, 6, 7, 2, 5)
print(tup.count(2))


# write a prigrame to check if list contain a palindrome of element (hint: use copy() method)
#             [1,2,3,2,1]             [1,"abc","abc", 1]


list1 = [1,2,3,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("NOT palendrome")