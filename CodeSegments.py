'''checking even'''

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

'''checking integer'''

def is_int(x):
    if x == int(x) :
        return True
    else:
        return False

'''summing digits of a number'''

def digit_sum(n):
    x = str(n)
    digits = []
    for i in x:
        i = int(i)
        digits.append(i)
    return sum(digits)

'''checking Factorial'''
def factorial(x):
    fact = x
    while x > 1:
        x = x - 1
        fact = x * fact
    return fact

'''checking prime'''

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x-1):
        if x % i == 0:
           return False
    return True

''' omitting vowels'''
def anti_vowel(text):
    str = ""
    for i in text:
        if i.lower() not in 'aeiouAEIOU':
            str += i
    return str

print anti_vowel("Hey look Words!")

'''scrabble score'''
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
    total = 0
    word = word.lower()
    for i in word:
        #print i
        for x in score:
            if x == i:
                total = total + score[x]
    return total

'''replace with asterix censored'''
def censor(text, word):
    result = text.split()
    result1 = []
    for char in result:
        if char == word:
            #print char
            char = "*" * len(word)
            #print char
        else:
            char = char
        result1.append(char)
    return " ".join(result1)
'''return the number of time an item occurs in a list'''
def count(sequence, item):
    total = 0
    for x in sequence:
        if item == x:
            total = total + 1
    return total
'''takes a list, then remove all odd numbers'''

def purify(li):
    new = []
    for item in li:
        if item % 2 == 0:
            new.append(item)
    return new

'''find product of the elements in a list'''
def product(li):
    mul = 1
    for item in li:
        mul = mul * item
    return mul

'''remove duplicate items in the list'''
def remove_duplicates(li):
    new_li = []
    for item in li:
        if item not in new_li:
            new_li.append(item)
    return new_li

'''finding median'''
def median(lst):
    lst.sort()
    list_len = len(lst)

    #even case
    if list_len % 2 == 0:
        y = list_len / 2
        #average of two elements surrounding the middle 
        average = (lst[y] + lst[y-1]) / 2.0
        return average

    # odd case 
    else: 
        # list_len - 1, since index starts at 0
        x = (list_len - 1) / 2
    return lst[x]

print median([4,5,5,4,6])  