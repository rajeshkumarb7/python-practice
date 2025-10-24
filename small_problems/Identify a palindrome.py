import re # for regular expression (regex)

def is_palindrome_onlycheckalpha_re(p):
    forward="".join(re.findall(r'[a-z]+',p.lower()))
    backward=forward[::-1]
    if(forward==backward):
        return True
    return False

"""
My solution uses the regular expressions module, which I import up top to extract letters from the input string.
 Within my is_palindrome function, I use the lower operator on the input string to convert all of the letters to lower case.
 And then I pass the result to the regular expressions find all function with a pattern that will search for a combination of one or more letters, A through Z.
 That will produce a list with all of the matched substrings, which I merged together into a single string using the join function, which represents my forward sequence of letters.
 On line five, I slice through that entire string with the stride set to negative one, which will give me a copy of the original string in reverse or backwards order.
 Finally, I compare the forward and backwards strings and return whether or not they're equal.


"""
def is_palindrome(s):
    s = str(s)  # convert to string in case input is a number
    s = s.lower().replace(" ", "")  # make it lowercase and remove spaces
    return s == s[::-1]
"""
🧠 Explanation:

s[::-1] reverses the string.

If original equals reversed → it’s a palindrome.

Simple, clean, one-liner logic.
"""
def is_palindrome_loop(s):
    s = str(s).lower().replace(" ", "")
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
"""
🧠 Explanation:

Compare characters from both ends.

Move inward each time.

If all match → palindrome.
"""

s="madam"
print(s)
print(is_palindrome(s))
print(is_palindrome_loop(s))
print(is_palindrome_onlycheckalpha_re(s))
print("------------")
s="go hang a salami - I'm a lasagna hog"
print(s)
print(is_palindrome(s))
print(is_palindrome_loop(s))
print(is_palindrome_onlycheckalpha_re(s))