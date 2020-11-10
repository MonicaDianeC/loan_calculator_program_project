# Name: Monica-Diane Constantino
# Date: 9/8/20
# Description: Programming Project #1 Loan Calculator
# TO DO:
# 1. Ask the user to input their loan amount, interest rate, and number of monthly payments for that loan.
# 2. Convert those values to floats and/or ints.
# 3. Divide the interest rate given by 1200 because the payments will be made monthly
# 4. Create and calculate the formula for the monthly payment
# 5. Output the values that the user gave and their monthly payment for their loan.
# 6. An additional calculation was for the total interest owed


# define constants
myName = "Monica-Diane Constantino, Software Engineer major"

# inputs
print("____________________________________________________________\n") #creates a border
loanAmount = float(input("How much is your loan amount? : $"))
rateWholeNum = float(input("How much is your interest rate? :"))
numMonths = int(input("How many months will you pay this loan? :"))
print("____________________________________________________________")
      
# process
interestRate = rateWholeNum / 1200
monthlyPayment = (interestRate * loanAmount) / (1 - ((1 + interestRate) ** -numMonths)) #loan payment formula
totalInterestOwed = (monthlyPayment * numMonths) - loanAmount #calculates the total interest owed

# outputs
print("____________________________________________________________\n")
print("Your name:", myName, "\n ")
loan_am = "Loan amount: ${:8.2f}".format(loanAmount)

# the loan amount is rounded off by two decimal places
print(loan_am)
i_rate = "Interest rate: {:4.2f}%".format(rateWholeNum)

# the interest rate is rounded off by two decimal places
print(i_rate)
print("Number of monthly payments:", numMonths)
mon_pay = "Monthly payment: ${:5.2f}".format(monthlyPayment)

# the loan amount is rounded off by two decimal places
print(mon_pay)
total_i_owed = "Total Interst Owed: ${:3.2f}".format(totalInterestOwed) # the total interest is rounded off by two decimalplaces
print(total_i_owed)
print("____________________________________________________________")
