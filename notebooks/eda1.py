import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
print(os.getcwd())

import sys
sys.path.append(r'C:\Users\hp\Desktop\New folder\Kifya AIM Training Program\Kaim-week-3\scripts')

# Import experience_analytics modules
from eda_task_1 import (
    load_data,
    summarize_data,
    check_missing_values,
    handle_missing_values,
    plot_histograms,
    plot_correlation_matrix,
    plot_boxplots,
    plot_scatter,
    plot_boxplot,
    plot_bar
)


import importlib
import eda

importlib.reload(eda)


data = load_data(r'C:\Users\hp\Desktop\New folder\Kifya AIM Training Program\Kaim-week-3\Data', delimiter='|')


# Summarize data
print("Data Information")
data.info()

print("Data Description")
data.describe()

 Check for missing values
check_missing_values(data)

# Handle missing values in the dataset
data = handle_missing_values(data)

# Relevant columns for analysis
insurance_columns = ['UnderwrittenCoverID', 'PolicyID']
client_columns = ['IsVATRegistered', 'Citizenship', 'LegalType', 'Title', 'Language', 'Bank', 'AccountType', 'MaritalStatus', 'Gender']
location_columns = ['Country', 'Province', 'PostalCode', 'MainCrestaZone', 'SubCrestaZone']
vehicle_columns = ['ItemType', 'Mmcode', 'VehicleType', 'RegistrationYear', 'Make', 'Model', 'Cylinders', 'Cubiccapacity', 'Kilowatts', 'Bodytype', 'NumberOfDoors', 'VehicleIntroDate', 'CustomValueEstimate', 'AlarmImmobiliser', 'TrackingDevice', 'CapitalOutstanding', 'NewVehicle', 'WrittenOff', 'Rebuilt', 'Converted', 'CrossBorder', 'NumberOfVehiclesInFleet']
plan_columns = ['SumInsured', 'TermFrequency', 'CalculatedPremiumPerTerm', 'ExcessSelected', 'CoverCategory', 'CoverType', 'CoverGroup', 'Section', 'Product', 'StatutoryClass', 'StatutoryRiskType']
payment_claim_columns = ['TotalPremium', 'TotalClaims']


# Plot histograms for numerical columns
plot_histograms(data, payment_claim_columns + ['SumInsured', 'CalculatedPremiumPerTerm'])

# Plot correlation matrix for selected columns
plot_correlation_matrix(data, payment_claim_columns + ['SumInsured'])

# Detect outliers in numerical data
numerical_columns = ['TotalPremium', 'TotalClaims', 'SumInsured', 'CalculatedPremiumPerTerm']
plot_boxplots(data, columns=numerical_columns)

# Plot scatter plots for analyzing relationships between premiums and claims
plot_scatter(data, x='TotalPremium', y='TotalClaims')
plot_scatter(data, x='CalculatedPremiumPerTerm', y='TotalClaims')

# Plot box plots to analyze the impact of location and vehicle type on claims
plot_boxplot(data, x='Province', y='TotalClaims')
plot_boxplot(data, x='VehicleType', y='TotalClaims')

# Plot bar plot to understand the distribution of premiums by vehicle type and gender
plot_bar(data, x='VehicleType', y='TotalPremium', hue='Gender')

