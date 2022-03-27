#%%
""" 
# Group A
Q.1.1 Write a piece of Python code that:
- Creates a dictionary: the keys of the dictionary should be even numbers from 10 to 30 (30
included), the values of the dictionary should be square roots of corresponding keys,
example, for keys in range (0, 4], the result would be {1: 1, 2: 1.41, 3: 1.73, 4: 2}
- Computes the product of the values in the dictionary created in point 1. If you don’t know
how to do the first part of the task, you can just write code for computing the product of
values in any dictionary  
"""
import math as m

dictionary = {k: m.sqrt(k) for k in range(10, 31)}
product = 1

for value in dictionary.values():
    product *= value
    
# alternative
dictionary = {}
prod = 1
for number in range(10, 31):
    dictionary[number] = m.sqrt(number)
    prod *= dictionary[number] # this operation could be done in another loop


#%%
# Group A
# Q.1.3

sentence = 'Today the temperature is 10 degrees'
# Using string methods or indexing and slicing, return the number included in sentence;
words = sentence.split()
number = words[-2]
print(number)
# Modify the variable sentence, so that instead of a value 10, there is a value 30
sentence_2 = sentence.replace('10', '30')
print(sentence_2)


#%%
""" Group A
Q2.1
Write a piece of Python code that:
1. Creates a list of cubed values (x3); the values that are cubed should be numbers divisible by
5 from range 5 to 100 (100 included) (x3), example for range (1, 10], the result would be:
[125, 1000]
2. Computes the product of the values in the list created in point 1. If you don’t know how to
do the first part of the task, you can just write code for computing the product of any list.
"""

cubed = [x ** 3 for x in range(5, 101) if x % 5 == 0]
prod = 1 
for number in cubed:
    prod *= number

# alteranative:
cubed = []
product = 1
for number in range(5, 101, 5):
    cubed.append(number ** 3)
    # we take the last available element, 
    # can be done in two loops as well, one loop is bit more efficient
    product *= cubed[-1] 


#%%
"""
Group A
Q2.3
Let sentence = ‘Today the temperature is 10 degrees’.
1. Using string methods or indexing and slicing, return the second word (‘the’) included in
sentence;
2. Modify a variable sentence, so that instead of a word degrees, there is a word
Fahrenheits
"""

sentence = 'Today the temperature is 10 degrees'
# we split the sentence by spaces and take the word with index 1 (second element of a resulting list: l1 = sentence.split(), l1[1])
word_the = sentence.split()[1]
print(word_the)
sentence_2 = sentence.replace('degrees', 'Fahrenheits')
print(sentence_2)

# looking for "the" with indexing:
word = sentence[6:9]
print(word)

# split in steps:
words = sentence.split()
w_the = words[1]


#%%
"""
Group B Q1.2
Write a script that:
Step 1. reads a string from the user.
Step 2. verifies if the string contains only letters
Step 3. prints “a first, o inside” when the first letter of the string is “a” and there is “o” somewhere in a
string, , “maybe a is first, maybe there is o” when “a” is first or there is a letter “o” occuring in the
string, or “There is no o in the string” otherwise.
"""

sentence = input("type some letters")

if sentence.isalpha(): # checks if only letters
    if sentence.startswith("a") and "o" in sentence:
        print("a first, o inside")
    elif sentence.startswith("a") or "o" in sentence:
        print("maybe a is first, maybe there is o")
    else:
        print("There is no o in the string")    
else:
    print("Not only letters!")


#%% 
"""
Group B Q1.3
Write a script that creates two list, list_1 and list_2: list_1 should contain all the odd numbers from 0 to
50, list_2 should contain all the even numbers from 30 to 100. Use the two lists to create one long list that would include
elements from list_1 and list_2. Do not nest the lists.
"""

list_1 = list(range(1, 50, 2)) # odd numbers in 0-50, so we must start with odd number in this range
list_2 = list(range(30, 101, 2))

list_3 = list_1 + list_2
# or
list_1.extend(list_2)
print(list_3, list_1)


#%%
"""
Group B Q2.2
Write a script that:
step 1. reads a string from the user,
step 2. counts how many times a digit 1 and 2 appers in it (separate counts for each digit)
step 3. prints “Even number of 1 and 2” when the 1 and 2 number is even, “Even number of 1 or
2” when one of the counts is even or “None of the counts is even” otherwise.
"""

some_characteres = input("type sth ")
count_1 = some_characteres.count("1")
count_2 = some_characteres.count("2")
if count_1 % 2 == 0  and count_2 % 2 == 0:
    print("Even number of 1 and 2")
elif count_1 % 2 ==0 or count_2 % 2 == 0:
    print("Even number of 1 or 2")
else:
    print("None of the counts is even")


#%%
"""
Group B Q2.3
Write a script that would verify how many common characters there are in two strings. (str_1 and str_2)
Count only unique characters. Print the answer.
"""
str_1 = "banana"
str_2 = "anna"

# solution 1: use sets to remove duplicates and find the common part
set_1 = set(str_1)
set_2 = set(str_2)

common_letters = set_1.intersection(set_2)
print(common_letters, len(common_letters))

# solution 2: use loops to go through one of the words and find letters in another
common_let = []
for letter in str_1:
    if letter in str_2 and letter not in common_let:
        common_let.append(letter)
print(common_let, len(common_let))

# same as solution2, using comprehensions and set:
common = [letter for letter in str_1 if letter in str_2]
common = set(common) # removes duplicates
print(common, len(common))
