"""
Given two lists, use the standard deviation function from numpy to determine
which language has the largest standard deviation. Usage will be np.std()
https://numpy.org/doc/stable/reference/generated/numpy.std.html
"""

"""
Dr. Forsyth's Code. Do Not Modify.
"""
# bring in randomness because we need it in our lives
import random
import numpy as np

# randomly sample a distribution between 20 and 100
random_length = int(random.uniform(20, 100))

# generate a random list of random length containing values up to 100
random_list_A = random.sample(range(100), random_length)

# generate a random list of random length containing values up to 100
random_list_B = random.sample(range(100), random_length)

# use the std() method from numpy to determine which list has the largest standard deviation

### YOUR CODE HERE

# Function to calculate standard deviation of an input list
def standard_deviation(input):
    stdev = np.std(input)  # Use numpy to compute standard deviation
    return stdev  # Return standard deviation

# Function to compare standard deviation of two input lists, returns list with larger standard deviation
def standard_deviation_compare(input_1, input_2):
    stdev_a = standard_deviation(input_1)  # Compute standard deviation of input 1
    stdev_b = standard_deviation(input_2)  # Compute standard deviation of input 2
    print("Standard Deviation A:", stdev_a)
    print("Standard Deviation B:", stdev_b)
    # Compare standard deviation values and return larger list
    if stdev_a > stdev_b:
        print(stdev_a, "is larger than", stdev_b)
        return input_1
    elif stdev_a < stdev_b:
        print(stdev_b, "is larger than", stdev_a)
        return input_2
    elif stdev_a == stdev_b:
        print("Values are equal")
        equal = True
        return equal


print("List Length:", random_length)
print("List A:", random_list_A)
print("List B:", random_list_B)

# set this variable equal to the list with the largest standard deviation
# do not modify this variable's name, you can/should adjust the contents ;)
# e.g. longest_list_is = myList

longest_list_is = standard_deviation_compare(random_list_A, random_list_B)
print("The Longest List is:", longest_list_is)
