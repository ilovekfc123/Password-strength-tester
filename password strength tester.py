import re

def test_password_strength(password):
    password_strength = 0
    if len(password) > 8:
        password_strength += 1
    if re.search(r'[0-9]', password):
        password_strength += 1
    if re.search(r'[a-z]', password):
        password_strength += 1
    if re.search(r'[A-Z]', password):
        password_strength += 1
    if re.search(r'[$&+,:;=?@#|<>.-^*()%!]', password):
        password_strength += 1
    
    if password_strength == 5:
        print("Strong Password")
    else:
        print("Weak Password")

while True:
  password = input("Enter a password: ")
  strength = test_password_strength(password)
