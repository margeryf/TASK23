import math                                   #in order to get to the math functions 


#Program that allows the user to access two different calculators : investment calculator or home loan repayment calculator 



# 1) the user should be allowed to choose which calculation they want to do.  
# investment - to calculate the amount of interest you'll earn on your investment 
# bond - to calculate the amount you'll have to pay on a home loan 
# Input : enter either "investment" or "bond" from the menu above to proceed: 


# 2) how the user capitalises their selection should not affect how the program proceeds i.e. "bond" "Bond" "BOND" or "investment" "Investment" "INVESTMENT",
# If the user doesnt type in a valid input, show an appropriate error message 


print ("Investment =  to calculate the the amount of interest you will earn on your investment")
print ("Bond = to calculate the amount you will have to pay on a home loan")    # to show the users what are the 2 options available  

choice = input ( "Dear Customer, enter either Investment or Bond to proceed: " ) 

rescribe_choice = choice.lower()
print(rescribe_choice)

if rescribe_choice == "investment" : 
    print( "You've chosen Investment") 
elif rescribe_choice == "bond" : 
    print("You've chosen Bond")
else: 
    print ("ERROR: Please enter your choice again")


#user selects "investment", ask the user to input: 
# the amount of money that they are depositing 
# the interest rate (as a percentage). Only the number of the interest rate should be entered - dont worry about having 
# to deal with the added "%" eg the user should enter 8 and not 8% 
# the number of years they plan on investing 
# then ask the user to input if they want "simple" or "compound", output the appropriate amount that they will get back
# after the given period, at the specified interest rate. (See the formula -- in dropbox) 
# print the answer 


if rescribe_choice == "investment" : 
    new_inv = float (input ("Enter the amount of money you are depositing: "))
    rate_inv = float (input ("Enter the interest rate: "))
    number_inv = float (input ("Enter the years they plan on investing: "))
    chosing_inv = input ("Please choose Simple or Compound: ")
    chosing_inv2 = chosing_inv.lower()
    r = rate_inv / 100 

    if chosing_inv2 == "simple" : 
        simple = new_inv * (1 + r*number_inv)
        print(round(simple, 2))

    elif chosing_inv2 == "compound" : 
        compound = new_inv * math.pow ((1+r),number_inv)
        print (round(compound, 2))

        #simple interest = A = P * (1 + r*t)
        # #compound interest = A = P * math. pow((1+r),t)
        # #r = interest rate divided by 100 (eg if 8 --> r =  0.08)
        # #P = amount the user deposit 
        # # t= number of years money is being invested 
        # # A = total amount once the interest has been applied

    #in case user chooses BOND ask: 
    # present value of the house 
    # interest rate 
    # the numb of months they plan to repay the bond (look bond formula)
    # calculate how much money the user will have to repay each month to repay the bond (output the answer)

elif rescribe_choice == "bond" : 
    new_bond= float( input ("Please enter the present value of the house: ") ) 
    rate_bond = float (input ("Please enter the interest rate: "))
    months_bond_repay= float (input ("Please enter in how many months you are planning to repay the bond: "))
    i = (rate_bond / 100) /12 
    repayment = ( i * new_bond) / (1 - (1 + i)** (-months_bond_repay))
    print (round(repayment, 2))


# bond formula = ( i * P ) / (1 - (1 + i)**(-n))
#p = present value , 
# i= monthly interest rate - calculated by dividing the annual interest rate by 12
#remeber to divide interest enteres by the user by 100 (eg 8/100) before dividing /12
#n = number of months over which the bond will be repaid 