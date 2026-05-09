# # function practice

# # 1. Create a function to print "Hello Python".

def print_hello_world():
    print("hello Python")
    
    
print_hello_world()

# # 2. Create a function that prints your name.

def print_name():
    name = input("enter your name :")
    print("your name is :" , name)
    
print_name()

# # 3. Write a function to add two numbers.

def sum_of_number(a,b):
    sum =  a + b
    print(sum)

sum_of_number(5,6)

# 4. Write a function to subtract two numbers.

def substract_of_number(a,b):
    sub = a - b
    print(sub)
    
# substract_of_number(6,6)

# 5. Create a function to multiply two numbers.

def mult_of_numbers(a,b):
    mult = a * b
    print(mult)
    
mult_of_numbers(5,5)

# 6. Write a function to divide two numbers.

def division_of_numbers(a,b):
    div = a // b
    print(div)
    
division_of_numbers(10,5)

# 7. Create a function to find the square of a number.

# def square_of_number(a):
    
    # method 1
    sqaure = a ** 2 
    print(sqaure)
    
    # method 2
    sqaure1 = a * a
    print(sqaure1)
    
square_of_number(5)

# 8. Create a function to find the cube of a number.

def cube_of_number(a):
    # method 1
    cube = a * a * a
    print(cube)
    
    # method 2
    cube1 = a ** 3
    print(cube1)
    
cube_of_number(3)

# 9. Write a function to check whether a number is even or odd.

def odd_or_even(a):
    result = print ("even") if a % 2 == 0 else print("odd")
        
odd_or_even(2)

# 10. Create a function to find the maximum of two numbers.

def max_of_number(a,b):
    max = print(f"{a} is bigger number ") if a > b else print(f"{b} is bigger")
    
max_of_number(1,11)
