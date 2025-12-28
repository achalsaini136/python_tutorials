#  dictonary in python.

info = {
    "name" : "achal saini",
    "subject" : ["python" , "c" , "java"],
    "topic" : ("dict" , "set"),
    "lerning" : "coding",
    "is_adult" : "no",
    "age" : "19"
}

print(type(info))
print(info)
print(info["name"])
print(info["topic"])
print(info["subject"])
print(info["age"])

info["name"] = "amit"       
info["surname"] = "saini"   # dictonary is mutable
print(info)

null_dict = {}
null_dict["name"] = "hello world"
null_dict["age"] = 19
print(null_dict)


# nested dictonary.

info = {
    "name" : "achal saini",
    "subject" : {
        "phy" : 70,
        "chem" : 80,
        "bio" : 81
    }
}

print(info["subject"]["chem"])


# set in python.

collection = {1, 2, 3, "hello", "world"}     # repeated word are ignored.
print(type(collection))
print(len(collection))
print(collection)


# for making a empty set correct syntax are required.

collection = set()
print(type(collection))

# set method

place = {"osahaka" , "hokkaido" , "tokyo" , "kyoto" , "japan"}

print(place.pop())
print(place.pop())

set1 = {"osahaka" , "hokkaido" , "tokyo" , "kyoto" , "japan"}
set2 = {1, 2, 3, 4, 5, 6,}

print(set1.union(set2))


set1 = {1, 2, 3, 4,}
set2 = {3, 4, 5, 6,}     # {2, 3}

print(set1.intersection(set2))