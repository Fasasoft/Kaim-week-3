import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path, delimiter='|'):
    """
    Load data from a text file with a specified delimiter.
    """
    data = pd.read_csv(file_path, delimiter=delimiter)
    return data

def check_missing_values(data):
    """
    Check for missing values in the dataset.
    """
    missing_values = data.isnull().sum()
    print("Missing Values:\n", missing_values)

def handle_missing_values(data):
    """ Handle missing values by imputing or removing.
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

def plot_histograms(data, columns):
    """
    Plot histograms for numerical columns.
    """
    for column in columns:
        data[column].hist(bins=30)
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

def plot_correlation_matrix(data, columns):
    """
    Plot correlation matrix for selected columns.
    """
    correlation = data[columns].corr()
    sns.heatmap(correlation, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()

def plot_boxplots(data, columns):
    """
    Plot box plots for numerical columns.
    """
    data.boxplot(column=columns)
    plt.title('Box Plot')
    plt.xticks(rotation=90)
    plt.show()

def plot_scatter(data, x, y, hue=None):
    """
    Plot scatter plot.
    """
    sns.scatterplot(data=data, x=x, y=y, hue=hue)
    plt.title(f'{x} vs {y}' + (f' by {hue}' if hue else ''))
    plt.show()

def plot_boxplot(data, x, y):
    """
    Plot box plot for categorical vs numerical columns.
    """
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=data, x=x, y=y)
    plt.title(f'{y} by {x}')
    plt.xticks(rotation=90)
    plt.show()

def plot_bar(data, x, y, hue):
    """
    Plot bar plot for categorical vs numerical columns with hue.
    """
    plt.figure(figsize=(12, 6))
    sns.barplot(data=data, x=x, y=y, hue=hue)
    plt.title(f'{y} by {x} and {hue}')
    plt.xticks(rotation=90)
    plt.show()