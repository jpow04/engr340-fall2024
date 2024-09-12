import math

"""
Use the Gauss-Legendre Algorithm to estimate Pi. Perform 10 approximation loops. Once complete, return the approximation.
:return:
"""

# a variable to hold your returned estimate for PI. When you are done,
# set your estimated value to this variable. Do not change this variable name
pi_estimate = 0

"""
Step 1: Declare and initialize all the values for the Gauss-Legendre algorithm
"""

# modify these lines to correct set the variable values
a = 1
b = 1/(math.sqrt(2))
p = 1
t = 1/4

# perform 10 iterations of this loop
for i in range(1, 10):
    """
    Step 2: Update each variable based upon the algorithm. Take care to ensure
    the order of operations and dependencies among calculations is respected. You
    may wish to create new "temporary" variables to hold intermediate results
    """

    ### YOUR CODE HERE ###

    # Algorithm processing
    a_n = (a + b) / 2
    b_n = math.sqrt(a * b)
    p_n = 2 * p
    t_n = t - p * (a_n - a) ** 2

    # Pi calculation
    pi_calculation = ((a_n + b_n) ** 2) / (4 * t_n)
    print("Iteration", i, "calculates pi as:", pi_calculation)

    # Reassign variables for next calculation
    a = a_n
    b = b_n
    p = p_n
    t = t_n

    # print out the current loop iteration. This is present to have something in the loop.
    print("Loop Iteration: ", i, "Complete")

"""
Step 3: After iterating 10 times, calculate the final value for PI
"""

# modify this line below to estimate PI
pi_estimate = pi_calculation

print("Final estimate for PI: ", pi_estimate)
print("Error on estimate: ", abs(pi_estimate - math.pi))
