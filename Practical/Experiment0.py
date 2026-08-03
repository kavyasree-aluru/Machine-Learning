#variables
x = 10
print(x)
print(type(x))
print()

y=0.18
print(y)
print(type(y))
print()

name = "Kavya"
print(name)
print(type(name))
print()

#conditional statements
age = 18
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")
print()

#loops
for i in range(10):
    print(i)
print()

count = 0
while count < 6:
    print(count)
    count += 1
print()

#operators
a=10
b=6
print("Addition:", a + b)
print()
print("Subtraction:", a - b)
print()
print("Multiplication:", a * b)
print()
print("Division:", a / b)
print()
print("OR operator:", a|b)
print()
print("AND operator:", a&b)
print()

#lists(mutable)
movies = ["Jersey", "Dragon", "Pokiri"]
print(movies)
movies.append("Bahubali")
print(movies)
print()

#tuples(immutable)
fruits = ("apple", "banana", "cherry")
print(fruits)
print()

#dictionaries
person = {
    "name": "Kavya",
    "age": 18,
    "city": "Hyderabad"
}
print(person)
print()
