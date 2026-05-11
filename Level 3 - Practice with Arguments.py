# Level 3 — Practice with Arguments in python

# 21. Write a function that accepts student name and marks and prints result.
def result(name,marks):
    if marks >= 40:
        print(f"{name} has passed with {marks}")
    else : 
        print(f"{name} has failer with {marks} better luck netx time")
result("monty",41)

# 22. Create a function that accepts unlimited numbers and returns their sum.
def find_sum(*numbers):
    return sum(numbers)
print(find_sum(5,5,5,5,10,5,5,5))

# 23. Write a function with default argument for country name.

def show_country(name, country_name = "india"):
    print(f"{name} is from {country_name}")
show_country("monty")

# 24. Create a calculator function using operator argument (+, -, *, /).
def calculator(a,b,operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a // b
    else :
        return "invalid operator"
    
print(calculator(5,5,'+'))
    
# 25. Write a function to swap two numbers.
def swap(a,b):
    return b ,a
print(swap(10,20))


#  26. Create a function to print multiplication table of any number.
def multiplication_table(n):
    for i in range(1,11):
        result = n * i  
        print(f"{n} * {i} = {result}")
multiplication_table(5)

# 27. Write a function to count uppercase and lowercase letters.
def count_letters(text):
    upper = 0
    lower = 0
    
    for char in text:
        if char.islower():
            lower += 1
        else :
            upper += 1
    print("uppercase letters : ",upper)
    print("lowercase characters : ",lower)
count_letters("hello WoRLd")
 
# 28. Create a function to remove duplicates from a list.
def remove_duplicate(my_list):
    return list(set(my_list))
print(remove_duplicate([1,1,1,1,1,2,2,2,2,2,3]))


# 29.  Write a function to sort a list.
def sort_list(my_list):
    return sorted(my_list)
print(sort_list([4,9,2,1,3]))

# 30. Create a function that returns both area and perimeter of rectangle.

def rectangle_details(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

print(rectangle_details(10,5))