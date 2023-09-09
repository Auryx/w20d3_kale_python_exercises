
# 1. Using the print method, print "Hello World"

# print('"Hello World"')

# 2. Create variables for the data type below. 
# Data Types:
# Int
# Float
# String
# Boolean 
# Boolean (The other boolean value)
# Lists ( 4 items in list min.)
# Dictionaries  ( 4 key/value pairs min.)

my_Int = 3
my_Float = 3.1
my_String = "3.14"
my_Boolean = True
my_OtherBoolean = False
my_List = ["1", "2", "3", "4"]
my_Dict = {
    "name" : "Paul",
    "age" : 21,
    "home" : "Kirkland, WA",
    "location" : "Honolulu, HI"
}

# 3. For each of the variables, use the print method for each variable. To print each varible

# print(my_Int, my_Float, my_String, my_Boolean, my_OtherBoolean, my_List)

# 4. Backtick ` in JS are used for Template literals. In a JS file a variable called intVariable and stringVariable exist.
# They are equal to the int and string variables on step 2.
# What is the python equvalent for: console.log(`int: ${intVariable}, string ${stringVariable}`)

# print(f"int: {my_Int}, string: {my_String}")

# 5. Comment out all print statements up to this point

# Done

# 6. Write a FOR LOOP in python that prints "David Rocks" 5 times
# Hint: type this into google "loop range python"

print("Problem: 6")
for x in range(5):
    print('"David Rocks"')

# 7. Declare a function what print "Alex Rocks". Invoke that function 5 times. 

print("Problem: 7")
def alex_rocks():
    print('"Alex Rocks"')

for x in range(5):
    alex_rocks() 

# 8. Declare a function that takes in 2 parameters. 
# It will print "P1(your parameter1) and P2(your parameter2) Rocks"
# Now call that function using "Kyle" and "Winston" as the arguments 
# invoke that function 4 more times

print("Problem: 8")
def people_rock(x, y):
    print(f'"P1 {x} and P2 {y} Rocks"')

people_rock("Kyle", "Winston")

for x in range(4):
    people_rock("Kyle", "Winston")

# Definitions:  
# P is for Placeholder. P is for Parameters.
# These 2 start w/ the letter P 
# A parameter is variable in the declaration of the function - The place holder

# A is for actual value. A is for aguement.
# These 2 start w/ the letter A
# Arguement is are the values when calling the function - The actual value

# 9. Remember the list variable in step 2. 
# a. Print the index at 3. Then comment it out
# b. Now print the index at 100. Does this error? comment it out
# e. Now print the index at -1 index. Observe what it prints. Then comment it out
# f. Now print the index at -100.  Does this error? comment it out

# print(my_List[3])
# print(my_List[100]) It returns "IndexError: list index out of range"
# print(my_List[-1]) Returns last item in list
# print(my_List[-100]) It returns "IndexError: list index out of range"
 
# 10. Write a FOR LOOP in python that prints each item in the list variable in step 2.  
# The staring number MUST be a negative number. The ending number MUST be postive number
# Looking to get each item printed once in order and then a second time in order

print("Problem: 10")
for x in range(8):
    print(my_List[x-4])

# 11. Write a WHILE LOOP in python that does the same thing as 10. 

print("Problem: 11")
x = 0
while x < 8:
    print(my_List[x-4])
    x += 1

# 12. For loops.
# Write a FOR LOOP in python that prints each item in list variable in step 2.  
# Hint: type this into google "loop python"

print("Problem: 12")
for x in my_List:
    print(x)

# 13. Repeat step 12 but instead of the list variable, use the dictionary variable. 
# Print each key

print("Problem: 13")
for x in my_Dict:
    print(x)

# 14. Repeat step 13. Instead of printing each key, print each value
# Hint: google "dictionary values python"

print("Problem: 14")
for x in my_Dict:
    print(my_Dict[x])
