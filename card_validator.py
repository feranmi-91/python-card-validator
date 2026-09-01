## This is the code for the card validator
print("{0:=^50s}".format(" Welcome "))

def luhn_steps(card_num):
    digits= card_num [::-1] 
    total =0

    for i, digit in enumerate(digits):
        digit = int(digit)
     
        
        if i %2 == 1:
            digit = digit *2
            if digit > 9:
                digit = digit - 9
            
        total = total + digit
    if total % 10 == 0:
        return True
    else:
        return False 
        


verve_1 = range(506099, 506198)
verve_2 = range(507865,507965)
verve_len = range(16,19)
master_c = range(51,55)
master_c1 = range(2221,2720)
master_len = 16

visa_c = 4
visa_len = (13,16,19)

def card_type(card_num):
    card_l = len(card_num)
    num= int(card_num[:6])
    
    m_num= int(card_num[:2])
    m_num1= int(card_num[:4])
    
    v_num= int(card_num[:1])

    if (num in verve_1 or num in verve_2) and card_l in verve_len:
        print("\nThe card is a verve card ")
       
    elif m_num in master_c or m_num1 in master_c1 and card_l == master_len:
        print("The card is a Master card")
    elif v_num == visa_c and card_l in visa_len:
        print("\nThe card is a Visa card")
    else:
        print('{0:~^40s}'.format("Enter a valid number "))
   
          
    return card_num
    
while True:
    card_num =  input("\nEnter your card number: ")
    print("\n")
    
    if not card_num.isdigit():
        print('{0:~^40s}'.format("Enter a valid number "))
        print('\n')
        
        continue
        
    if luhn_steps(card_num):
        print("Your card is valid")
        card_type(card_num)
    else:
       print('{0:~^40s}'.format("Enter a valid number "))  
