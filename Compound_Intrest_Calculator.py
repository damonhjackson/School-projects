
# Prompt the user to enter P, r, n, and t
p = float(input("Please enter the principle amount:"))
r = float(input("Please enter the interest rate. ex.10 for %10: "))
n = float(input("Please enter the number of compounding periods per year: "))
t = float(input("Please enter the amount of years : "))

# Calculate the Compound Interest(FV)
FV = p * ((1 + ((r/100.0)/n)) ** (n*t))

# Display original principle (P)
p_string = '${:,.2f}'.format(p)
print("Original Principle: ", p_string)

# The amount of interest earned
interest_earned = (FV - p)
ie_string = '${:,.2f}'.format(interest_earned)
print("Interest Earned: ", ie_string)

# The total value of the account at the end of the term
fv_string = '${:,.2f}'.format(FV)
print("Total value of account: ", fv_string)
