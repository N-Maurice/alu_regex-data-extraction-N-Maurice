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
 

with open("text.txt", "r") as file:
    data = file.read()

email_regex = r"\b[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z0-9._]{2,}\b"
email_match = re.findall(email_regex, data)

if email_match:
    for emails in email_match:
        print(emails)
else:
    print("No email founds")

#........................................................................................................
#  Finding URL
url_regex = r"https?:\/\/(?:www\.)?[a-zA-Z0-9?.\-_*+#*]+\.[a-zA-Z]{2,}(?:\/\S*)?"

url_match = re.findall(url_regex, data)

if url_match:
    for url in url_match:
        print(url)
else:
    print("No URLS found")


#........................................................................................................
# Finding Hashtag
hashtag_regex = r"\#[a-zA-z0-9_-+=!@#$%^&*()<>]*"

hashtag_match = re.findall(hashtag_regex, data)

if hashtag_match:
    for hashtag in hashtag_match:
        print(hashtag)
else:
    print("Hashtag not found")
