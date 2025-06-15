# 1.Find the length of a string without using len()

text = "Priyanka"
count = 0

for ch in text:
    count += 1

print("Length of string:", count)

# 2. Find the count of 'a's in a given input

text = "banana is a fruit"
count = 0

for ch in text:
    if ch == 'a':
        count += 1

print("Count of 'a':", count)

# 3.Reverse a string (without slicing)

text = "Python"
reversed_text = ""

for ch in text:
    reversed_text = ch + reversed_text

print("Reversed:", reversed_text)

# 4.text = "Python"
reversed_text = ""

for ch in text:
    reversed_text = ch + reversed_text

print("Reversed:", reversed_text)

# 4. Count number of vowels (a, e, i, o, u)

text = "education is powerful"
vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Vowel count:", count)


