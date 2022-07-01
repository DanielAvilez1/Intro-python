# this is a comment
# single line

# variables
name = "Daniel"
last_name = "Avilez"
age = 101
price = 12.21
found = False
valid = True

print("Hi there, my name is " + name)
print ("and my age is:" + str(age) )

# if statement
if age < 100:
    print("no worries, you are still young!")
elif age == 100:
    print("wow! you got to a century")
else:
    print("Sorry, you are getting a little old now")    

# functions

def hello():
    print("line 1")
    print("line 2")
    print("line 3")



def say_hello():
    print("Hello there:")    


print("line 4")

hello() # function call

say_hello()
say_hello()
say_hello()