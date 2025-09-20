import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.sample(chars, k=length))   
    return password

print(generate_password())



