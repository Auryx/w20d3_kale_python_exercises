

# 1. Write a program that sum of all elements:
one = [613, 955, 291, 497, 562, 483, 165, 210, 864, 789]

print("Problem: 1")
print(sum(one))

# 2.  Write a program that find the largest element:
two = [386, 850, 274, 316, 526, 937, 998, 249, 269, 922]

print("Problem: 2")
two.sort()
print(two[-1])

# 3. Write a program that duplicates that doubles the value of each elements in the list:
# for example: [1,2,3] should result in [2,4,6]
three = [211, 36, 295, 455, 147, 977, 381, 253, 327, 617]

print("Problem: 3")
def doubler(x, y):
        return (y[x] * 2)
print(doubler(0, three))

# 4. Write a program that concatenates these two list into a single list:
four_a = [582, 427, 534, 143, 567, 604, 12, 48, 686, 825]
four_b = [357, 728, 406, 989, 380, 800, 201, 410, 452, 141]

print("Problem: 4")
def concat(x, y):
        z = x + y
        return z
print(concat(four_a, four_b))

# 5. Write a program that removes a specific element from a list by its value.
five = [456, 942, 944, 762, 836, 451, 314, 559, 954, 211]

print("Problem: 5")
five.remove(456)
print(five)

# 6. Write a program that removes a specific element from a list by its index.
six = [993, 245, 896, 250, 226, 313, 918, 877, 793, 695]

print("Problem: 6")
def index_removal(temp_list, temp_value):
        del temp_list[temp_value]
        return temp_list
print(index_removal(six, 0))

# 7. Write a program that sorts a list of numbers in ascending order.
seven = [887, 106, 368, 603, 35, 455, 728, 449, 108, 47]

print("Problem: 7")
def sorter(x):
        x.sort()
        return x
print(sorter(seven))

# 8. Write a program that filters out all elements in a list that are less than a specified value.
# use for loop and conditionals
eight = [309, 122, 27, 240, 453, 174, 193, 649, 804, 171]
threshold = 200

print("Problem: 8")
def thresher(y):
    counter = 0
    temp_list = []
    y.sort()
    y.reverse()
    for x in y:
        if(x > threshold):
               
               temp_list.insert(counter, x)
        else:
               y.clear()
               y = temp_list
        counter += 1
    return y
print(thresher(eight))
              

# 9. Calculate and print the length (number of elements) of a given list.
nine = [679, 697, 657, 171, 503, 582, 656, 82, 724, 796]

print("Problem: 9")
def length_calc(x):
    return len(x)
print(length_calc(nine))

# 10. Write a program that take a list and print a subset of its elements by specifying a start and end index.
ten = [64, 800, 662, 185, 630, 612, 181, 210, 738, 12]
start_index = 1
end_index = 4

print("Problem: 10")
def sub_list(temp_list, x, y):
    a_list = []
    counter = x
    while counter <= y:
            a_list.append(temp_list[counter])
            counter += 1
    return a_list
print(sub_list(ten, start_index, end_index))

# 11. Write a program iterates the list and
# prints 'FizzBuzz' when divisable by 3 and 5.  
# prints 'Fizz' when divisable by 3 .  
# prints 'Buzz' when divisable by 5. 
eleven = [213, 927, 265, 39, 860, 421, 550, 884, 991, 1500]

print("Problem: 11")
def fizzbuzz(y):
    final = ""
    for x in y:
            if x % 3 == 0:
                final += "Fizz"
            if x % 5 == 0:
                final += "Buzz"
    return final
print(fizzbuzz(eleven))

# 12. Write a program that appends an element to the end of a list.
twelve = [36, 632, 155, 350, 746, 642, 113, 534, 9, 34]

print("Problem: 12")
def appender(x, y):
      x.append(y)
      return x
print(appender(twelve, 42))

# 13. Write a program that inserts an element at a specific position in a list.
thirteen = [191, 871, 990, 163, 687, 747, 606, 799, 373, 851]
element_to_insert = 4

print("Problem: 13")
def inserter(x, y, z):
      x.insert(y, z)
      return x
print(inserter(thirteen, 3, element_to_insert))

# 14. Write a program that counts how many times a specific element appears in a list.
fourteen = [1, 1, 1, 2, 2, 1, 3, 3, 2, 1]
element_to_count = 1

print("Problem: 14")
def list_counter(temp_list, countee):
    counter = 0
    for x in temp_list:
        if (x == countee):
              counter += 1
    return counter
counted = list_counter(fourteen, element_to_count)
print(f"The amount of times that {element_to_count}\n appears in {fourteen}\n is {counted} time(s)")

def list_counter2(temp_list, countee):
    counter = temp_list.count(countee)
    print(f"{countee} appears a total of {counter} time(s)")
list_counter2(fourteen, element_to_count)
      

# try using for loop and conditional
# and then try .count() method


# 15.  Write a program that extracts all even numbers from a list and stores them in even_only:
# use for loop and conditionals
fifteen = [267, 688, 88, 755, 680, 746, 559, 710, 283, 451]
even_only = []

print("Problem: 15")
def even_steven(temp_list):
    global even_only
    for x in temp_list:
        if (x % 2 == 0):
              even_only.append(x)
    return even_only
print(even_steven(fifteen))



# 16. Write a program that reverses this list but does not change the original sixteen variable:
# The answer is not sixteen.reverse(). 
sixteen = [378, 763, 856, 566, 847, 795, 313, 540, 67, 219]

print("Problem: 16")
def reverser(y):
    new_list = []
    for x in y:
            new_list.insert(0, x)
    return new_list
print(reverser(sixteen))

# 17. Write a flattens this double nested listbelow:
# Result should be [1, 2, 3, 4, 5, 6, 7, 8]
# Hint: try a nested loop (2 for in loops) 
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]

print("Problem: 17")
def flattener(y):
    result_list = []
    for i in range(len(y)):
        for j in y[i]:
            result_list.append(j)
    return result_list
print(flattener(nested_list))

            

# 18. Write a program that finds duplicates from the 2 lists below:
# Hint: try a nested loop (2 for in loops) and use equality
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

print("Problem: 18")
def dupes(y, z):
    result = {
        "values" : [],
        "indices" : [[ ], [ ]],
        "is_duped" : False
    }
    for i in y:
        for j in z:
            if (i==j):
                result["indices"][0].append(y.index(i))
                result["indices"][1].append(z.index(j))
                result["values"].append(j)
                result["is_duped"] = True
    return result

possibly_duped = dupes(list1, list2)
print(possibly_duped)