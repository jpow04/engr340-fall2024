import pandas as pd
import numpy as np
from scipy.stats import norm, chisquare, ttest_ind, ttest_1samp
import matplotlib.pyplot as plt

"""
Preamble: Load data from source CSV file
"""
# set file location
filename = r"\all_participant_data_rsi.csv"
path_to_data_folder = r"C:\Users\powelj\Documents\GitHub\engr340-fall2024\data\drop-jump"
full_path_to_file = path_to_data_folder + filename
df = pd.DataFrame(pd.read_csv(full_path_to_file, delimiter=',', header=0))  # load and set pandas dataframe

"""
Question 1: Load the force plate and acceleration based RSI data for all participants. Map each data set (accel and FP)
to a normal distribution. Clearly report the distribution parameters (mu and std) and generate a graph two each curve's 
probability distribution function. Include appropriate labels, titles, and legends.
"""
print('-----Question 1-----')

# Load force plate and acceleration data
force_plate_rsi = df['force_plate_rsi'].to_numpy()  # Convert force plate data to numpy array
acceleration_rsi = df['accelerometer_rsi'].to_numpy()  # Convert acceleration data to numpy array

# Compute normal distributions for force plate and acceleration data
fp_mu, fp_std = norm.fit(force_plate_rsi)
acc_mu, acc_std = norm.fit(acceleration_rsi)

# Report distribution parameters
print(f"Force Plate Distribution Parameters: mu =", fp_mu, "std =", fp_std)
print(f"Accelerometer Distribution Parameters: mu =", acc_mu, "std =", acc_std)

x_rsi = np.linspace(start=-0.5, stop=2, num=10000)  # PDF x axis
fp_pdf = norm.pdf(x_rsi, fp_mu, fp_std)  # Force plate PDF
acc_pdf = norm.pdf(x_rsi, acc_mu, acc_std)  # Acceleration PDF

# Plot probability distribution functions
plt.plot(x_rsi, fp_pdf, label='Force Plate RSI')
plt.plot(x_rsi, acc_pdf, label='Accelerometer RSI')
plt.title('Probability Distribution Functions')
plt.xlabel('RSI')
plt.ylabel('Counts')
plt.legend()
plt.grid()
plt.show()
# Created from distribution-fit.py example

"""
Question 2: Conduct a Chi2 Goodness of Fit Test for each dataset to test whether the data is a good fit
for the derived normal distribution. Clearly print out the p-value, chi2 stat, and an indication of whether it is 
a fit or not. Do this for both acceleration and force plate distributions. It is suggested to generate 9 bins between 
[0,2), add append -inf and +inf to both ends of the bins. An alpha=0.05 is suitable for these tests.
"""
print('\n\n-----Question 2-----')

bins = np.linspace(0, 2, 9)  # Generate 9 bins between [0,2)
bins = np.r_[-np.inf, bins, np.inf]  # append -inf and +inf to both ends of the bins

"""
Acceleration
"""

expected_acc_prob = np.diff(norm.cdf(bins, loc=acc_mu, scale=acc_std))  # CDF difference gives probabilities for each bin

expected_acc_counts = expected_acc_prob * len(acceleration_rsi)  # Expected frequency for each bin

observed_acc_counts, observed_acc_edges = np.histogram(acceleration_rsi, bins=bins, density=False)  # place observations into bins

chi2_acc, p_acc = chisquare(f_obs=observed_acc_counts, f_exp=expected_acc_counts, ddof=2)  # Conduct chi2 test

print(f"Acceleration Chi2 Values: chi2 =", chi2_acc, "p =", p_acc)  # Print out p-value and chi2 stat
if p_acc < 0.05:  # Compare p-value with alpha of 0.05
    print("Not a fit, p value is less than alpha 0.05")
else:
    print("Fit, p value is greater than alpha 0.05")

"""
Force Plate
"""

expected_fp_prob = np.diff(norm.cdf(bins, loc=fp_mu, scale=fp_std))  # CDF difference gives probabilities for each bin

expected_fp_counts = expected_fp_prob * len(force_plate_rsi)  # Expected frequency for each bin

observed_fp_counts, observed_fp_edges = np.histogram(force_plate_rsi, bins=bins, density=False)  # place observations into bins

chi2_fp, p_fp = chisquare(f_obs=observed_fp_counts, f_exp=expected_fp_counts, ddof=2)  # Conduct chi2 test

print("Force Plate Chi2 Values: chi2 =", chi2_fp,  "p =", p_fp)  # Print out p-value and chi2 stat
if p_fp < 0.05:  # Compare p-value with alpha of 0.05
    print("Not a fit, p value is less than alpha 0.05")
else:
    print("Fit, p value is greater than alpha 0.05")
# Created from chi-square-dist-fit.py example

"""
Question 3: Perform a t-test to determine whether the RSI means for the acceleration and force plate data are equivalent 
or not. Clearly report the p-value for the t-test and make a clear determination as to whether they are equal or not.
"""
print('\n\n-----Question 3-----')

stat, p_value = ttest_ind(acceleration_rsi, force_plate_rsi, alternative='two-sided')  # Conduct two-sided t-test

print("p-value =", p_value)  # Report stat and p-value
if p_value > 0.05:  # Check if p-value is greater than alpha 0.05
    print("Means are equal")
else:
    print("Means are not equal")
# Created from Module 5.2 - T-Tests.pdf

"""
Question 4 (Bonus): Calculate the RSI Error for the dataset where error is expressed as the difference between the 
Force Plate RSI measurement and the Accelerometer RSI measurement. Fit this error distribution to a normal curve and 
plot a histogram of the data on the same plot showing the fitted normal curve. Include appropriate labels, titles, and 
legends. The default binning approach from matplot lib with 16 bins is sufficient.
"""

rsi_error = force_plate_rsi - acceleration_rsi  # Calculate RSI error
error_mu, error_std = norm.fit(rsi_error)  # Fit RSI error to normal distribution
x_error = np.linspace(start=-0.5, stop=0.5, num=10000)  # Error x axis
error_pdf = norm.pdf(x_error, error_mu, error_std)  # Error y axis

plt.hist(rsi_error, bins=16, label='RSI Error Histogram')  # Generate RSI error histogram
plt.plot(x_error, error_pdf, label='Fitted Normal Curve')  # Plot error distribution curve
plt.xlabel('Relative RSI Error')
plt.ylabel('Counts')
plt.title('Distribution of RSI Error')
plt.show()
# Created from distribution-fit.py example
