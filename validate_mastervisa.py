#Filename:validate_mastervisa.py
#Description:validate a user input MasterCard or VISA credit card number
#Author: Goh Jia Ying

#define validate programe
def validate(card_no):
    sum_values=0
    for i in range(1,17,2):
        check = card_no[i]*2
        
        if check > 9:
            new_digit = check -9
            sum_values = sum_values + new_digit
            
        else:
            new_digit = check
            sum_values = sum_values + new_digit
            
    for i in range(0,16,2):
        sum_values = sum_values + card_no[i]

    if sum_values%10 ==0:

        return True
    
    else:
        return False

        
#obtain a card number from user
cardno = str(input("Enter credit card no: "))

# loop until it is a valid card number

valid_card_no = False
while not valid_card_no:
    

    #check if input is digits
    if not cardno.isdigit():
        print("Credit Card must be only in digits.")
        cardno = str(input("Enter credit card number:"))
        
    #check if input is 16 numbers    
    elif len(cardno) != 16:
        print("Not 16 digits. Please enter 16 digits.")
        cardno = str(input("Enter credit card number:"))

    #Not valid visa or master if not start with 4 or 51
    elif not 50 < int(cardno[0:2]) < 56 and not int(cardno[0]) == 4:
        print("Not a mastercard or Visa card number.")
        cardno = str(input("Enter credit card number:"))

    #Not valid visa or master if check sum if wrong.
    elif validate(cardno)== False:
        print("Not a valid mastercard or Visa card number.")
        cardno = str(input("Enter credit card number:"))

    #Return is Master card if start with 51-55 , end loop
    elif  50 < int(cardno[0:2]) < 56:
        print("This is a Mastercard.")
        valid_card_no = True

    #Return is Visa if start with 4, end loop
    elif int(card_no[0])==4:
        print("This is a Visa.")
        valid_card_no = True


## 1234567891234567
## 1438537782264165
        
