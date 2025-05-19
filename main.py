#!/usr/bin/env python3
"""
This application uses Regex to extract information from:
- Email addresses
- URLs
- Phone numbers
- Credit card numbers
- Hashtags
"""

import re

with open("text.txt", "r") as file:
    data = file.read()

# Prompt the user for what they want to search
while True:
    print("What would you like to search for?\n")
    print("_____________________________________\n")
    print("1. Emails only")
    print("2. URLs only")
    print("3. Hashtags only")
    print("4. Phone numbers only")
    print("5. Credit cards only")
    print("6. Exit")
    print("_______________________________________\n")

    try:
        choice = int(input("Enter your choice from 1 to 6\n"))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")
        continue

    if choice == 1:
        # Finding emails
        email_regex = r"\b[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z0-9._]{2,}\b"
        email_match = re.findall(email_regex, data)

        if email_match:
            for email in email_match:
                print(email)
        else:
            print("No emails found")

    elif choice == 2:
        # Finding URLs
        url_regex = (
            r"https?:\/\/(?:www\.)?[a-zA-Z0-9?.\-_*+#*]+\."
            r"[a-zA-Z]{2,}(?:\/\S*)?"
        )
        url_match = re.findall(url_regex, data)

        if url_match:
            for url in url_match:
                print(url)
        else:
            print("No URLs found")

    elif choice == 3:
        # Finding hashtags
        hashtag_regex = r"#\w+"
        hashtag_match = re.findall(hashtag_regex, data)

        if hashtag_match:
            for hashtag in hashtag_match:
                print(hashtag)
        else:
            print("No hashtags found")

    elif choice == 4:
        # Searching for a phone number
        phone_nbr_regex = (
            r"\+?(?:\(\d{1,}\)|\d{3})[\s.-]?\d{3}[\s.-]?\d{3,4}"
        )
        phone_nbr_match = re.findall(phone_nbr_regex, data)

        if phone_nbr_match:
            for phone_number in phone_nbr_match:
                print(phone_number)
        else:
            print("No phone numbers found")

    elif choice == 5:
        # Browsing for credit cards
        credit_card_nbr_regex = (
            r"\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}"
        )
        credit_card_nbr_match = re.findall(credit_card_nbr_regex, data)

        if credit_card_nbr_match:
            for credit_card_number in credit_card_nbr_match:
                print(credit_card_number)
        else:
            print("No credit card info available")

    elif choice == 6:
        print("Exiting the application")
        break

    else:
        print("Invalid input. Please choose between 1 and 6.")
        continue
