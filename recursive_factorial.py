__author__ = 'Rick'
def factorial(number):
    if number <= 1:  #base case
        return 1
    else:  # if the number is greater take it and call the function again with (n-1).
        return number * factorial(number - 1)

user_input = eval(input("enter a non-negative number: "))
factorial_of_user_input = factorial(user_input)
print(factorial_of_user_input)
