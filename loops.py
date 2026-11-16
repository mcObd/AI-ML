# for loop
for i in range(0, 20, 2):
    print(i)

names = ["john", "Micheal", "David"]
for name in names:
    print(name)

persons = {"a":'Sarah', 'b':'Davish', 'c':'John'}
for person in persons.keys():
    print(person)

row = range(1, 11)
i = 0
while i<len(row):
    print(i)
    i += 1

x = '50'
print(type(x))
x = int(x)
print(type(x))

# Lists
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[0:5])
print(numbers[3:-2])
num=7
column=[
    1,

]