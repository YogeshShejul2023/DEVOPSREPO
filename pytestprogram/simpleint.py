# Get user inputs
principal = float(input("Enter the principal amount: $"))
years = int(input("Enter the number of years: "))
interest_rate = float(input("Enter the annual interest rate (as a percentage): "))

# Convert interest rate from percentage to decimal
interest_rate_decimal = interest_rate / 100

# Calculate simple interest
simple_interest = principal * interest_rate_decimal * years

# Calculate total payable amount
total_payable = principal + simple_interest

# Display the result


print(total_payable)
