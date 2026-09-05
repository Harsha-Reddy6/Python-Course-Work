import re
'''fullname=input("Enter the full name: ")
pattern=r'^[A-Za-z]{2,25}( [A-Za-z]{2,25})+$'
res=re.fullmatch(pattern,fullname)
print("Valid full name" if res else "invalid full name")'''

# email=input("Enter the email: ")
# pattern=r'^[A-Za-z0-9._]+@[A-Za-z0-9._]+\.[a-zA-Z]{2,}$'
# res=re.fullmatch(pattern,email)
# print("Valid email" if res else "invalid email")

# number=input("Enter the number: ")
# pattern=r'^(?:\+91|0)?[6-9]\d{9}$'
# res=re.fullmatch(pattern,number)
# print("Valid number" if res else "inavalid number")

# password=input("Enter the password: ")
# pattern=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}'
# res=re.fullmatch(pattern,password)
# print("Valid password" if res else "inavalid password")

# username=input("Enter the username: ")
# pattern=r'^[A-Za-z0-9_]{4,15}'
# res=re.fullmatch(pattern,username)
# print("Valid username" if res else "invalid username")

# aadhar_number=input("Enter the aadhar_number: ")
# pattern=r'^[0-9]{4}\s[0-9]{4}\s[0-9]{4}'
# res=re.fullmatch(pattern,aadhar_number)
# print("Valid aadhar_number " if res else "invalid aadhar_number")

pancard=input("Enter the pan number: ")
pattern=r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
res=re.fullmatch(pattern,pancard)
print("Valid pancard " if res else "invalid pancard")