import random
import string

def random_password_generator(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = "".join(random.choice(characters) for _ in range(length))
    return random_string

while True:
    try:
        password_length = int(input("Enter the desired length of the password: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

random_string = random_password_generator(password_length)
print (random_string)
