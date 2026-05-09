
# 11. Write a function to return the sum of three numbers.

def sum_of_three_no(a,b,c):
    return a + b + c

s = sum_of_three_no(5,5,5)
print(s)

# 12.  Create a function to return the factorial of a number.
# Factorial of number = the factorial of a non-negative integer is the product of all positive integers less than or equal to that number. It is represented by the symbol !.
# eg 5! = 5 * 4 * 3 * 2 * 1      


def factorial_of_number(n):
    # method 1 - using for loop
    result = 1
    for i in range(2,n+1):
        if n > 0:
            result = result * i  
            # # 1 * 2 = 2   2 * 3 = 6  6 * 4 = 24 24 * 5 = 120
    print(result) 
    
    # method 2 - while loop 
    looping = 2
    result1 = 1      
    iterator = 2  
    while looping <= n :
        result1 = result1 * iterator 
        iterator += 1
        looping += 1
    print(result1)
       
factorial_of_number(5)    

# method 3 
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

p = factorial_recursive(5) # Output: 120
print(p)

# 13.Write a function to return the reverse of a string.


def rev_string(s):
    # method 1 
    print(s[::-1])
    
    # method 2
    rev = ""
    for i in range(1,len(s)+1):
        char = s[-1]
        rev = rev + char
        s = s[:-1]
    print(rev)
    
rev_string("Python")

# 14. Create a function to count vowels in a string.
# vowels = a , e , i , o , u

def count_vowels(s):
    # method 1 
    count = 0
    vowels = ['a','e','i','o','u','A','P','P','L','E']
    for char in s:
        if char in  vowels:
            vow_in_str = char 
            print(vow_in_str)
            count += 1
    print(f"the number of vowels in {s} is : {count}")
    
    # method 2
    return len([char for char in s if char in 'AEIOUaeiou'])
    

count_vowels("Apple")  
print(count_vowels("vowelSapple"))

# 15. Write a function to check whether a number is prime.
# prime numbers = A prime number is a whole number greater than 1 that can only be divided evenly by 1 and itself.

# Not a "Composite": If a number can be divided by something else (like 6, which is 2 * 3), it’s called a composite number.

def prime_no(n):
    exact_divisor = []
    divisor = [1,n]
    for i in range(1,n+1):
        if n % i == 0 : 
            exact_divisor.append(i)
    print(exact_divisor)

    if exact_divisor == divisor:
        print(f"{n} is prime number")
    else :
        print (f"{n} is not prime number")
        
prime_no(8)

# 16.Create a function to find the largest number in a list.


def max_no():
    list1 = [ 45,87,12,45,36,52,25 ]
    
    list1.sort()     
    print(f"the largest number in list is {list1[-1]}")
    
    # 1. Assume the first one is the biggest
    max_no = list1[0]
    for num in list1:
        if num > max_no :
            max_no = num   
    print(f"Largest number in the list is {max_no}")   
max_no()

# 17. Write a function to calculate the average of list elements.
    
def average_numbers():
    list1 = [2,5,6,8,9,7]   
    average = sum(list1) / len(list1)
    print(f"average of number is {average}")
average_numbers()

def method2():   
    
    list2 = [2,5,6,8,9,7]
    index = 0
    sum = 0
        
    while index < len(list2) :
        sum = sum + list2[index]
        index += 1     
    average = sum / len(list2)
    print(f"average of number is {average}")    
method2()    
    
def method3():
    sum = 0
    list3 = [2,5,6,8,9,7]
    for num in list3 :
        sum = sum + num
    average = sum / len(list3)
    print(f"avareg of number is {average}")
method3()

# 18. Create a function to convert Celsius to Fahrenheit.

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example usage:
temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)

print(f"{temp_c}°C is equal to {temp_f}°F") 


# 19. Write a function to calculate simple interest.

def Calculate_simple_interest(principle,rate,period):
    SI = (principle * rate * period) / 100
    print(f"simple interest of principal amount {principle} is {SI}")
    
Calculate_simple_interest(1000,5,2)

# 20. Create a function to check whether a string is palindrome.
# palindrome number - A palindrome number is a number that reads the same forward and backward.Examples of Palindrome Numbers: 121  (Reversed: 121) — Palindrome 

def is_palindrome(n):
    temp = n
    reversed_num = 0 
    while n > 0 :
        digit = n % 10 
        reversed_num = (reversed_num * 10) + digit
        n = n // 10
           
    if temp == reversed_num:
        print("number is palindrome")
    else: 
        print("number is not palindrome")
is_palindrome(121)

