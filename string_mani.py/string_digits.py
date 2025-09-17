import random, string

user_input = "12345"

#  Check if the string contains only digits
if all(c in string.digits for c in user_input):
    print("Only digits")  

#  Generate a random 6-digit string
random_number = ''.join(random.choice(string.digits) for _ in range(6))
print(random_number)       



