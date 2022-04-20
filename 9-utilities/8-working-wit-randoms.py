import random
import string

print(random.random())

print(random.randint(10,25))

print(random.choice([10,23,34,45,56,67,78,89]))

print(random.choices([10,23,34,45,56,67,78,89],k=2))

def generate_random_password():
    random_password="".join(random.choices(string.ascii_lowercase+string.ascii_uppercase+string.digits,k=6));
    return random_password

print(generate_random_password())