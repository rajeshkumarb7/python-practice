def get_prime_factors(number):
    factors=[]
    divisor=2
    while number>=divisor:
        if number%divisor==0:
            number//=divisor
            factors.append(divisor)
        else:
            divisor+=1
    return factors

"""
🧠 Explanation:
        while loop
        Fast & memory efficient
        Best for large numbers

Start dividing n by 2 (the first prime).

If it divides evenly, record it and divide n down.

Move to the next divisor.

Stop when n becomes 1.

The result is all the prime factors.

"""

def get_prime_factors_re(n, divisor=2):
    """Return the list of prime factors of n (recursive version)."""
    if n == 1:
        return []
    if n % divisor == 0:
        return [divisor] + get_prime_factors_re(n // divisor, divisor)
    else:
        return get_prime_factors_re(n, divisor + 1)
"""
🧠 Explanation for reursive:
            Clean & elegant logic
            Might hit recursion limit for very large numbers
Base case: if n == 1, return an empty list.

If divisor divides n, include it and recurse with n // divisor.

Otherwise, try the next divisor (divisor + 1).

Each recursive call builds the list step by step
"""
n=int(input("enter the number for find prime factors:"))
print(get_prime_factors(n))
print(get_prime_factors_re(n))



"""
from linkedin course
 Your goal is to write a Python function to find the prime factorization of a given number.
 It should take an integer value as the input and then return a list containing all of its prime factors.
 
 For example, calling the function with an input of 630 should return a list containing the values 2, 3, 3, 5, 7.
   Those are all prime numbers and if you multiply them together, their product is 630.

 Calling your function on a prime number like 13, should return a list with just a single value, that prime number.

 I decided to search for factors by dividing the given number by sequentially larger values, starting from two, To see which ones divide evenly into it without leaving a remainder behind.

 For example, if the input to my function is the number 60, I'll first try dividing that by two.
 The quotient is an even 30 with no remainder, so I'll add two to a list of factors I found.
 Next I'll try dividing that result of 30 by two again, and the quotient is 15, no remainder left over.
 So I'll add two to my list of found factors again.
 Trying to divide 15 by two leaves a remainder or fractional value.
 So I'll increment the divisor and try again.
 Three divides cleanly into 15, so I'll add that to my list and continue the search.
 This process continues until I eventually find all of the prime factors.
 You can see that process in the code for my get prime factors function.

 (video game blips) Line two instantiates a list to hold the found factors and line three sets the initial divisor value to two.
 After that, a while loop continues to iterate as long as the divisor is less than the input number that I'm trying to divide it by.
 The if statement on line five uses the modulo operator to check if the current divisor divides into that number without a remainder, and if so I append it to the factors list and set the new value of number to be the quotient for the next loop iteration.
 If that divisor was not a factor, then I increment the divisor variable and try again.
 Finally, after the while loop reaches its exit condition, the function returns the assembled list of factors.
 
"""