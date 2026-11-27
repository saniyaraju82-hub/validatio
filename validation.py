import re
email=input("enter email")
email_pattern=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9_]+\.[a-ZA-Z0]{2}"
if re.full match(email_pattern,email)
print("valid email")
else:
print("invalid email")
phone=input("enter phone number")
phone number_pattern=r"[0-9][6-9]{9}"
if re.full match(phone number_pattern,phone number)
print("valid phone number")
else:
print("invalid phone number")
log """
payment successfull TXN12345
payment failed TXN67890
payment refund 
"""
ids=re.findall (r"TXN[0-9]+",log)
print("transaction IDs:",result)

