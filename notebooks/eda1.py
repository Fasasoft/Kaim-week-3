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

