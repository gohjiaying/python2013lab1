#Filename: master_or_visa.py
#Description: Algorithm to categorize if a user credit card is visa or mastercard
#Author: Goh Jia Ying

#Allow user to input number
card_no = str(input("Please enter your credit card number:"))

#If first number is 4 and len is 16, the card is visa
if int(card_no[0]) == 4 and len(card_no) == 16:
    print("Card is Visa")

#if first 2 numbers is between 50 and 56 and len is 16 it is mastercard
elif 50 < int(card_no[0:2]) < 56 and len(card_no) == 16:
    print("Card is MasterCard")
    
#Else , it is not visa nor mastercard
else:
    print("Card is not visa or master")

