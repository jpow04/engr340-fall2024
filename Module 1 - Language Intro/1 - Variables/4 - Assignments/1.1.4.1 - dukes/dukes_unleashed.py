"""
For investments over $1M it can be typically assumed that they will return 5% forever.
Using the [2022 - 2023 JMU Cost of Attendance](https://www.jmu.edu/financialaid/learn/cost-of-attendance-undergrad.shtml),
calculate how much a rich alumnus would have to give to pay for one full year (all costs) for an in-state student
and an out-of-state student. Store your final answer in the variables: "in_state_gift" and "out_state_gift".

Note: this problem does not require the "compounding interest" formula from the previous problem.

"""

### Your code here ###

# Create dictionary for in state tuition and assign values
InState = {
    'TuitionFees': 13376,
    'Housing': 5772,
    'Meals': 6268,
    'BooksSupplies': 1176,
    'Transportation': 1968,
    'PersonalCosts': 2156,
    'LoanFees': 76
}

# Create dictionary for out of state tuition and assign values
OutState = {
    'TuitionFees': 30466,
    'Housing': 5772,
    'Meals': 6268,
    'BooksSupplies': 1176,
    'Transportation': 1968,
    'PersonalCosts': 2156,
    'LoanFees': 76
}

# Function to calculate required gift given 5% interest rate
def required_gift(tuition):
    gift_total = tuition / 0.05
    return gift_total


in_state = []  # Create list of in state tuition costs
out_state = []  # Create list of out of state tuition costs

# Assign corresponding values to the lists
in_state += InState.values()
out_state += OutState.values()

# Sum tuition costs and assign to variables
in_state_tuition_costs = (sum(in_state))
out_state_tuition_costs = (sum(out_state))

# Print tuition costs
'''print("in-state tuition: ", in_state_tuition_costs)
print("out-of-state tuition: ", out_state_tuition_costs)'''

# Run required_gift function
in_state_gift = required_gift(in_state_tuition_costs)
out_state_gift = required_gift(out_state_tuition_costs)
print("in-state gift: ", in_state_gift)
print("out-of-state gift: ", out_state_gift)
for x in OutState:
    print(x, ":", OutState[x])
