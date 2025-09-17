import string

text = "Hello, world!!!"
clean = ''.join(c for c in text if c not in string.punctuation)

print(clean)  # Output: "Hello world"
