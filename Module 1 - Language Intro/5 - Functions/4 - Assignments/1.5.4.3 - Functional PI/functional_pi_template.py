import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    ### YOUR CODE HERE ###

    a = 1
    b = 1 / (math.sqrt(2))
    p = 1
    t = 1 / 4

    acceptable = False

    while acceptable == False:
        a_n = (a + b) / 2
        b_n = math.sqrt(a * b)
        p_n = 2 * p
        t_n = t - p * (a_n - a) ** 2

        # Pi calculation
        pi_calculation = ((a_n + b_n) ** 2) / (4 * t_n)

        # Reassign variables for next calculation
        a = a_n
        b = b_n
        p = p_n
        t = t_n

        error = abs(math.pi - pi_calculation)

        if error < abs(target_error):
            return pi_calculation
        else:
            print("Solution is not acceptable, Performing next iteration")


desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
