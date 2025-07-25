# str1 = "hello world"

# print(type(str1))
# print(len(str1))

# print(str1[0:4])
# print(str1[0:len(str1)])
# print(str1[-4:-2])

# str1 = str1.capitalize()
# print(str1)
# str1 = str1.upper()
# print(str1)
# str1 = str1.lower()
# print(str1)
# str1 = str1.title()
# print(str1)
# str1 = str1.find("L")
# print(str1)

# x = str(input("enter a number : "))
# print(x)


''' IF ELSE ElIF '''

# a = 200
# b = 200
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

# # one line if statement
# if a > b: print("a is greater than b")

# # short if else statement
# print("A") if a > b else print("B")
# print("A") if a > b else print("B") if a == b else print("C")

# # logical operator
# d = 200
# e = 33
# f = 500
# if d > e and f > d:
#   print("Both conditions are True")
# if d > e or d > f:
#   print("At least one of the conditions is True")
# if not d > e:
#   print("a is NOT greater than b")

# # emptying an if statement
# if b > a:
#    pass


''' LIST AND TUPPLE '''

# cities = ["fsd ", "lhr ", "karachi ", "rwl ", "gujrat ", "isl "]
# print("welcome to ", cities[5])

# # adding or changing elements

# cities.append("sgd ")
# print(cities)

# # or
# cities = cities + ["quetta ", "peshawar"]
# print(cities)

# # or
# cities.insert(0, "mltn ")
# print(cities)

# # or
# cities[0] = "multan"
# print(cities)

# # taking slices out of a list
# city = cities[1:5]
# print(city)

# # or
# city1 = city[2:]
# print(city1)

# # or
# city2 = city[:2]
# print(city2)

# # deleting and removing elements
# print(cities)
# del cities[3]
# print(cities)

# # or
# cities.remove("lhr ")
# print(cities)

# # popping elements
# cities1 = cities.pop(1)
# print(cities1)
# print(cities)

# # or
# cities.append(cities1)
# print(cities)
# print(cities1)

# # TUPPLES
# # in tupple you cannot change, edit, add or remove it like you do in list
# print("\n Tupples ")
# cars = ("civic ", "toyota ", "volvo ", "haval ")
# car_fav = cars[0]
# print(car_fav)


'''LOOPS'''

# for num in range(1,21):
#     print(num)

# first_names = ["BlueRay ", "Upchuck ", "Lojack ","Gizmo ", "Do-Rag "]
# for a in first_names:
#     print(a)

# x = 3
# while x <= 9:
#     print(x)
#     x+=1


'''DICTIONARY'''

# cars = {
#     "brand": "dodge",
#     "model": ["charger", "challenger "],
#     "year": 2024
# }
# cars["type"] = "new"
# print(cars)

# print(cars["model"][1])
# print(cars["brand"])

# del cars["model"]
# print(cars)
# print(len(cars))

# # or
# dictionary = dict(brand="dodge", model="charger", year=2024)
# print(dictionary)

# for i in dictionary.values():
#     print(i)
# for x in dictionary.keys():
#     print(x)
# for y, z in dictionary.items():
#     print(y, z)

# customers = [
# {
# "customer id": 0,
# "first name":"John",
# "last name": "Ogden",
# "address": "301 Arbor Rd.",
# },
# {
# "customer id": 1,
# "first name":"Ann",
# "last name": "Sattermyer",
# "address": "PO Box 1145",
# },
# ]
# print(customers[0]["address"])

# customers545 = {
# 0 : {
# "first name":"John",
# "last name": "Ogden",
# "address": "301 Rd.",
# },
# 1 : {
# "first name":"Ann",
# "last name": "Sattermyer",
# "address": "PO Box 1145",
# }
# }
# print(customers545[0]["address"])


'''FUNCTIONS'''

