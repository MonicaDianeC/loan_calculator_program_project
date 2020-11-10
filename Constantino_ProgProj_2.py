# Name: Monica-Diane Constantino
# Date: 10/6/20
# Description: Loan Calculator 2.0 Programming Project #2
# TO DO:
# 1. create a function that asks the user for a loan amount
# 2. create a function that asks the user for the term (in months) of the loan
# 3. create a function that determines the interest based on loan amount and monthly term
# 4. create a function that calculates the monthly payment
# 5. in main(), call and initialize these functions and call calc_monthly_pay() from loan_calculator module
#               format and print these values
#               run program at least 21 times for error checking


# functions

# gets the loan amount
def get_loan():

    loan = float(input("Please enter a loan amount that is at least $500: $"))

    while loan < 500:
        loan = float(input("Invalid amount. \nPlease re-enter a loan amount that is at least $500: $"))

    return loan

# get the monthly term
def get_term():

    term = int(input("Please enter the monthly term (6 to 48 months): "))

    while term < 6 or term > 48:
        term = int(input("Invalid monthly term. \nPlease re-enter a monthly term that is between 6 to 48 months: "))

    return term

# determine interest rate
def get_interest(amount, months):
    
    if amount >= 500 and amount <= 2500:
        if months >= 6 and months <= 12:
            rate = 8
        elif months >= 13 and months <= 36:
            rate = 10
        elif months >= 37 and months <= 48:
            rate = 12
            
    elif amount >= 2501 and amount <= 10000:
        if months >= 6 and months <= 12:
            rate = 7
        elif months >= 13 and months <= 36:
            rate = 8
        elif months >= 37 and months <= 48:
            rate = 6
            
    elif amount >= 10001:
        if months >= 6 and months <= 12:
            rate = 5
        elif months >= 13 and months <= 36:
            rate = 6
        elif months >= 37 and months <= 48:
            rate = 7       

    return rate

# calculate the monthly payment
def calc_monthly_pay(whole_num_rate, amount_of_loan, num_months):
    
    rate_applied = whole_num_rate / 1200            
    calculation = (rate_applied * amount_of_loan) / (1 - ((1 + rate_applied) ** -num_months))         

    return calculation

# main function
def main():

    # loan calculation values
    loan_amount = get_loan()
    monthly_term = get_term()
    interest_rate = get_interest(loan_amount, monthly_term)
    monthly_payment = calc_monthly_pay(interest_rate, loan_amount, monthly_term)

    # format headings and data
    column_list = ["Loan Amount", "Monthly Term", "Interest Rate", "Monthly Payment"]
    for headings in column_list:
        print(headings, end = "\t")
    message = "${:5.2f} \t {} months\t{:>5}%\t\t${:5.2f}".format(loan_amount, monthly_term, interest_rate, monthly_payment)
    print('\n',message)
    print("                                                 ")

main()

