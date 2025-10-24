
s="mango apple oRange bAnanNA "

def sorted_string_detailed(inputs):
    words=inputs.split()
    words=[w.lower()+ w for w in words]
    words.sort()
    words=[w[len(w)//2:] for w in words]
    return " ".join(words)
"""
🔍 Example walkthrough:

s = "mango apple oRange bAnanNA"

Split words → ['mango', 'apple', 'oRange', 'bAnanNA']

Make lowercase + original →
['mangomango', 'appleapple', 'orangeoRange', 'banannabAnanNA']

Sort (based on lowercase) →
['appleapple', 'banannabAnanNA', 'mangomango', 'orangeoRange']

Remove lowercase part (keep original) →
['apple', 'bAnanNA', 'mango', 'oRange']

Join result → "apple bAnanNA mango oRange"
"""

def sorted_string(words):
    return " ".join(sorted(words.split(),key=str.casefold))
"""
💡 Explanation:

words.split() → break string into words

sorted(..., key=str.casefold) → sort words case-insensitively (ignores upper/lower differences)

" ".join(...) → combine back to a single string
"""

print("string: ",s)
print("detailed code: ",sorted_string_detailed(s))
print("simple code: ",sorted_string(s))