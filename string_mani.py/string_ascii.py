import random, string

# Pick a random letter (uppercase or lowercase)
letter = random.choice(string.ascii_letters)
print(letter)  

# Check if all characters in "HelloWorld" are letters
result = all(c in string.ascii_letters for c in "smart")
print(result)  
