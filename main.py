#!/usr/bin/env python3
""" 
This application is using Regex to extracting information from : 
Email addresses
URLs
Phone numbers
Credit card numbers
Time in 12-hour or 24-hour format
HTML tags
Hashtags
Currency amounts
"""
import re
 
email_regex = r"\b[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z0-9._]{2,}\b"

with open("forms.txt", "r") as file:
    data = file.read()

email_match = re.findall(email_regex, data)

if email_match:
    for emails in email_match:
        print(emails)
else:
    print("No email founds")