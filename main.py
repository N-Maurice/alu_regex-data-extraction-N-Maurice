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

# Prompt the user for what they want to search
while True:
    print("What would you like to search for? \n")
    print("_____________________________________\n")
    print("1. Emails only")
    print("2. URLs only")
    print("3. Hashtags only")
    print("4. Phone numbers only")
    print("5. Credit cards only")
    print("6. Exit")
    print("_______________________________________\n")

    choice = int(input("Enter your choice from 1 to 6\n"))
 
    if choice == 1:
        #1 Finding emails
        email_regex = r"\b[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z0-9._]{2,}\b"
        email_match = re.findall(email_regex, data)

        if email_match:
            for emails in email_match:
                print(emails)
        else:
            print("No email founds")
            
    elif choice == 2:
        #2  Finding URL.......................................................................................
        url_regex = r"https?:\/\/(?:www\.)?[a-zA-Z0-9?.\-_*+#*]+\.[a-zA-Z]{2,}(?:\/\S*)?"

        url_match = re.findall(url_regex, data)

        if url_match:
            for url in url_match:
                print(url)
        else:
            print("No URLS found")
    
    elif choice == 3:
        #3 Finding Hashtag
        hashtag_regex = r"#\w+"
        hashtag_match = re.findall(hashtag_regex, data)

        if hashtag_match:
            for hashtag in hashtag_match:
                print(hashtag)
        else:
            print("Hashtag not found")
    
    elif choice == 4:
        #4 Searching for a phone number:
        phone_nbr_regex = r"\+?(?:\(\d{1,}\)|\d{3})[\s.-]?\d{3}[\s.-]?\d{3,4}"


        phone_nbr_match = re.findall(phone_nbr_regex, data)

        if phone_nbr_match:
            for phone_number in phone_nbr_match:
                print(phone_number)
        else:
            print("No Phone Number Available To Display!!")
    
    elif choice == 5:
        #5 Browsing for credit cards:
        credit_card_nbr_regex = r"\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}"


        credit_card_nbr_match = re.findall(credit_card_nbr_regex, data)

        if credit_card_nbr_match:
            for credit_card_number in credit_card_nbr_match:
                print(credit_card_number)
        else:
            print("No Credits Card Info Available")
    
    elif choice == 6:
        print("Exiting the application")
        break

    else:
        print("Invalid Input. Please choose between 1-6")
        continue
