# data types
x = 10
y = 20.90
String = "Hello"
isMale = True

# list
students = ["John", "Mcquendie", "Jane"]

# dictionary
bio = {'name' : "John", "age" : 30, "isMale" : True}
person = dict(one = 'victor', two = 'jane')

# set
Ai_class_absent ={'joy', 'jane'}

# tuple
people = tuple(("mac", "joy"))

print(x,y)
print(String)
print(isMale)
print(students)
print(bio)
print(Ai_class_absent)
print(people)

# # control flow
# username = input("Enter your name: ")
# if username == "John":
#     print(f'Welcome {username}')
# elif len(username) <5:
#     print("Name must be at least 5 characters long")
# else:
#     print("You know what? only john is allowed")

# loops
userinput = int(input("Enter your number : "))
a = 1
mul = 1
while a <= 10:
    mul = userinput * a
    print(f'{userinput} * {a} = {mul}')
    a += 1

