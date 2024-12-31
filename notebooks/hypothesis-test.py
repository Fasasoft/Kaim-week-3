import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
print(os.getcwd())

import sys
sys.path.append(r'C:\Users\hp\Desktop\New folder\Kifya AIM Training Program\Kaim-week-3\scripts')

# Import experience_analytics modules
from testingh import (
    load_data
)

import importlib
import testingh

importlib.reload(testing1)



import pandas as pd

# Load the data
data = pd.read_csv(r'C:\Users\hp\Desktop\New folder\Kifya AIM Training Program\Kaim-week-3\Data\MachineLearningRating_v3.txt', delimiter='|')

# Display the first few rows of the data
data.head()

# Check for null values
null_values = data.isnull().sum()
print("Null Values:\n", null_values)

# Handling missing values
# Drop columns with more than 50% missing values
threshold = len(data) * 0.5
data = data.dropna(thresh=threshold, axis=1)

# Impute missing values for categorical data with mode
for column in data.select_dtypes(include=['object']).columns:
    data[column].fillna(data[column].mode()[0], inplace=True)

# Impute missing values for numerical data with mean
for column in data.select_dtypes(include=['number']).columns:
    data[column].fillna(data[column].mean(), inplace=True)

# Verify there are no more missing values
null_values_after = data.isnull().sum()
print("Null Values after Handling:\n", null_values_after)

# Summary of the data
data.info()
data.describe()


import testing1 as abt

# Get unique values for segmentation
unique_provinces = data['Province'].unique()
unique_postalcodes = data['PostalCode'].unique()

print("Unique Provinces:\n", unique_provinces)
print("Unique Postal Codes:\n", unique_postalcodes)


provinces_a = ['Gauteng', 'KwaZulu-Natal', 'Mpumalanga', 'Eastern Cape', 'Western Cape']
provinces_b = ['Limpopo', 'North West', 'Free State', 'Northern Cape']
zipcodes_a = [1459, 1513, 1619, 1625, 1629]
zipcodes_b = [1852, 1982, 2007, 2066, 4093]


provinces_a = ['Gauteng', 'KwaZulu-Natal', 'Mpumalanga', 'Eastern Cape', 'Western Cape']
provinces_b = ['Limpopo', 'North West', 'Free State', 'Northern Cape']
zipcodes_a = [1459, 1513, 1619, 1625, 1629]
zipcodes_b = [1852, 1982, 2007, 2066, 4093]

# Evaluate each hypothesis separately with detailed logging

# Hypothesis 1: There are no risk differences across provinces
data['Province_Group'] = data['Province'].apply(lambda x: 'Group_A' if x in provinces_a else ('Group_B' if x in provinces_b else 'Other'))
group_a_provinces = data[data['Province_Group'] == 'Group_A']
group_b_provinces = data[data['Province_Group'] == 'Group_B']
print(f"Size of Group A (Provinces): {len(group_a_provinces)}, Size of Group B (Provinces): {len(group_b_provinces)}")

p_value_provinces = abt.evaluate_hypothesis(data, 'Province_Group', ['Group_A'], ['Group_B'], 'TotalClaims', 't-test')
print(f"Province hypothesis p-value: {p_value_provinces}")



# Hypothesis 2: There are no risk differences between zip codes
data['ZipCode_Group'] = data['PostalCode'].apply(lambda x: 'Group_A' if x in zipcodes_a else ('Group_B' if x in zipcodes_b else 'Other'))
group_a_zipcodes = data[data['ZipCode_Group'] == 'Group_A']
group_b_zipcodes = data[data['ZipCode_Group'] == 'Group_B']
print(f"Size of Group A (ZipCodes): {len(group_a_zipcodes)}, Size of Group B (ZipCodes): {len(group_b_zipcodes)}")

p_value_zipcodes = abt.evaluate_hypothesis(data, 'ZipCode_Group', ['Group_A'], ['Group_B'], 'TotalClaims', 't-test')
print(f"ZipCode hypothesis p-value: {p_value_zipcodes}")

# Hypothesis 3: There are no significant margin (profit) differences between zip codes
data['Margin'] = data['TotalPremium'] - data['TotalClaims']
p_value_margin = abt.evaluate_hypothesis(data, 'ZipCode_Group', ['Group_A'], ['Group_B'], 'Margin', 't-test')
print(f"Margin hypothesis p-value: {p_value_margin}")



# Hypothesis 4: There are no significant risk differences between Women and Men
group_a_gender = data[data['Gender'] == 'Female']
group_b_gender = data[data['Gender'] == 'Male']
print(f"Size of Group A (Women): {len(group_a_gender)}, Size of Group B (Men): {len(group_b_gender)}")

p_value_gender = abt.evaluate_hypothesis(data, 'Gender', ['Female'], ['Male'], 'TotalClaims', 't-test')
print(f"Gender hypothesis p-value: {p_value_gender}")

# Compile and analyze results
results = {
    'Provinces': p_value_provinces,
    'ZipCodes': p_value_zipcodes,
    'Margin': p_value_margin,
    'Gender': p_value_gender
}

# Analyze results
abt.analyze_results(results)