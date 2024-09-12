"""
This problem requires you to calculate compounding interest and final value of a  US treasury deposit based upon
current interest rates (that will be provided). Your analysis should return the final value of the investment
after a 10-year and 20-year period. The final values should be stored in the variables "ten_year_final"
and "twenty_year_final", respectively. Perform all your calculations in this file. Do not perform the calculations by hand
and simply write in the final result.

Prompt: On October 27th, 2022, Elon Musk purchased Twitter for $44B in total, with reportedly $33B of his own money. Since
that time, it appears this investment has not worked out. If Elon has instead bought $44B of US Treasury Bonds, how much
would his investment be worth in 10-year and 20-year bonds? Assume the 10-year bonds pay 3.96%,
the 20-year bonds pay 4.32%, with each compounding annually.
"""

### all your code below ###

def ten_year_bond(principal):  # Function to calculate 10-year bonds
    ten_year_final = principal * (pow((1 + 3.96 / 100), 10))
    return ten_year_final

def twenty_year_bond(principal):  # Function to calculate 20-year bonds
    twenty_year_final = principal * (pow((1 + 4.32 / 100), 20))
    return twenty_year_final


bonds_bought = 33000000000
ten_year_final = ten_year_bond(bonds_bought)
twenty_year_final = twenty_year_bond(bonds_bought)
print("10-year bonds will be worth: $", ten_year_final)
print("20-year bonds will be worth: $", twenty_year_final)
