import re
email_conditions="^[a-z]+[/._]?[a-z 0-9]+[@]/w+[.]/w{2,3}$"
user_email = input("Enter your email: ")
if re.search(email_conditions,user_email):
    print("Valid email")
else:
    print("Invalid email")