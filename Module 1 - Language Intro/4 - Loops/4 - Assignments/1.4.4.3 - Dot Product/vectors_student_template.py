import random
import numpy as np


# copy in Dr. Forsyth's random list function for use
def generate_random_int_list(list_length, upper_bound):
    # given the length above, sample the Natural Numbers up to upper_bound that many times
    randoms = random.sample(range(upper_bound), list_length)

    # return the generated list
    return randoms


"""
Step 1: Generate two "vectors" of equal length but full of random values
"""
max_length = 10
maximum_value = 100
fixed_length = int(random.uniform(2, max_length))
vector_a = generate_random_int_list(fixed_length, maximum_value)
vector_b = generate_random_int_list(fixed_length, maximum_value)

"""
Step 2: Iterate through the vector(s) and calculate the dot product
"""

# store your result here. Do not change the name
dot_product = 0

### Your code here

def compute_dot_product(vector_1, vector_2):
    """
    Computes the dot product of two vectors of equal length
    :param vector_1: list of integers
    :param vector_2: list of integers
    :return: dot product of the two vectors
    """
    vector_length = len(vector_1)  # Compute the length of the vectors
    dot_product = 0  # Declare dot product
    for i in range(vector_length):  # Repeat calculation for all vector values
        dot_product += vector_1[i] * vector_2[i]  # Multiply corresponding values in each vector and add to dot product
    return dot_product  # Return dot product


print("Vector A is:", vector_a)
print("Vector B is:", vector_b)
dot_product = compute_dot_product(vector_a, vector_b)
print("Dot Product is:", dot_product)

"""
Step 3: Calculate the error of your dot_product compared with numpy's solution
"""
# check code with numpy...
a_np = np.asarray(vector_a)
b_np = np.asarray(vector_b)

# use dot product from numpy to check this result
correct = np.dot(a_np, b_np)
error = correct - dot_product

# compare results
print("Your result: ", dot_product)
print("Correct result: ", correct)
print("Error: ", error)
