import re
email = input("What's your email? ").strip()

if re.search(".+2@.+", email):
    print("Valid")
else:
    print("Invalid")    