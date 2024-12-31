import pandas as pd
from scipy.stats import ttest_ind, chi2_contingency

def load_data(file_path, delimiter='|'):
    """
    Load data from a text file with a specified delimiter.
    """
    data = pd.read_csv(file_path, delimiter=delimiter)
    return data

def handle_missing_values(data):
    """
    Handle missing values in the dataset.
    """
    # Drop columns with more than 50% missing values
    threshold = len(data) * 0.5
    data = data.dropna(thresh=threshold, axis=1)

    # Impute missing values for categorical data with mode
    for column in data.select_dtypes(include=['object']).columns:
        data[column].fillna(data[column].mode()[0], inplace=True)

    # Impute missing values for numerical data with mean
    for column in data.select_dtypes(include=['number']).columns:
        data[column].fillna(data[column].mean(), inplace=True)
    
    return data

def check_hypothesis(group_a, group_b, metric, test_type):
    """
    Perform hypothesis testing on two groups.
    """
    # Check if sample sizes are sufficient
    size_a = len(group_a)
    size_b = len(group_b)
    if size_a < 30 or size_b < 30:
        print(f"Sample size too small for valid {test_type} (less than 30). Size A: {size_a}, Size B: {size_b}")
        return None

    if test_type == 't-test':
        t_stat, p_value = ttest_ind(group_a[metric], group_b[metric])
    elif test_type == 'chi-squared':
        contingency_table = pd.crosstab(group_a[metric], group_b[metric])
        chi2, p_value, dof, expected = chi2_contingency(contingency_table)
    else:
        raise ValueError("Unsupported test type")
    
    return p_value

def evaluate_hypothesis(data, feature, group1_values, group2_values, metric, test_type):
    """
    Evaluate a single hypothesis based on the given data.
    """
    # Ensure group1_values and group2_values are lists
    if not isinstance(group1_values, list):
        group1_values = [group1_values]
    if not isinstance(group2_values, list):
        group2_values = [group2_values]
    
    print(f"Evaluating hypothesis for feature: {feature}, Group 1 values: {group1_values}, Group 2 values: {group2_values}")

    group_a = data[data[feature].isin(group1_values)]
    group_b = data[data[feature].isin(group2_values)]
    
    # Debugging statements
    print(f"Group A sample size: {len(group_a)}")
    print(f"Group B sample size: {len(group_b)}")

    p_value = check_hypothesis(group_a, group_b, metric, test_type)
    return p_value

def analyze_results(results):
    """
    Analyze and report the results of hypothesis testing.
    """
    for hypothesis, p_value in results.items():
        if p_value is None:
            print(f"Unable to test {hypothesis} due to insufficient sample size.")
        elif p_value < 0.05:
            print(f"Reject the null hypothesis for {hypothesis}.")
        else:
            print(f"Fail to reject the null hypothesis for {hypothesis}.")