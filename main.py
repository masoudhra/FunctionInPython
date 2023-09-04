# kalame def neshoon dahandeye function dar python hast
def say_hello(name, age):
    print("Hello " + name + ". You are " + str(age))
    print("I am here!")

def add_numbers(a, b):
    c = a + b
    return c

num1 = 10
num2 = 15

first_name = "Masoud"
age = 33
print("===========================")
say_hello(first_name, age)
result = add_numbers(num1, num2)
print(result)
print("===========================")