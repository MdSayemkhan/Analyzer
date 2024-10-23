# Let's start with the structure of the data analysis library.
# This is a skeleton of the classes and functions we'll define.

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder

class DataAnalyzer:
    
    def __init__(self, data):
        self.data = data

    # Data Loading functions
    @classmethod
    def load_csv(cls, file_path):
        return cls(pd.read_csv(file_path))
    
    @classmethod
    def load_excel(cls, file_path):
        return cls(pd.read_excel(file_path))
    
    @classmethod
    def load_json(cls, file_path):
        return cls(pd.read_json(file_path))

    # Data Cleaning functions
    def handle_missing(self, strategy='drop', fill_value=None):
        if strategy == 'drop':
            self.data.dropna(inplace=True)
        elif strategy == 'fill':
            self.data.fillna(fill_value, inplace=True)
        return self
    
    def remove_duplicates(self):
        self.data.drop_duplicates(inplace=True)
        return self

    def convert_dtypes(self, columns, dtype):
        self.data[columns] = self.data[columns].astype(dtype)
        return self
    
    # Exploratory Data Analysis (EDA)
    def summary_statistics(self):
        return self.data.describe()
    
    def correlation_matrix(self):
        return self.data.corr()
    
    def plot_distribution(self, column):
        plt.figure(figsize=(8, 6))
        sns.histplot(self.data[column], kde=True)
        plt.title(f"Distribution of {column}")
        plt.show()
    
    def plot_correlation_heatmap(self):
        plt.figure(figsize=(10, 8))
        sns.heatmap(self.correlation_matrix(), annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title('Correlation Heatmap')
        plt.show()

    # Feature Engineering
    def normalize(self, columns):
        scaler = StandardScaler()
        self.data[columns] = scaler.fit_transform(self.data[columns])
        return self
    
    def one_hot_encode(self, columns):
        encoder = OneHotEncoder(sparse=False)
        encoded_data = pd.DataFrame(encoder.fit_transform(self.data[columns]), 
                                    columns=encoder.get_feature_names_out(columns))
        self.data = self.data.drop(columns, axis=1).join(encoded_data)
        return self
    
    # Utility Functions
    def split_data(self, target_column, test_size=0.2):
        X = self.data.drop(target_column, axis=1)
        y = self.data[target_column]
        return train_test_split(X, y, test_size=test_size, random_state=42)

    def detect_outliers(self, column, method='iqr'):
        if method == 'iqr':
            Q1 = self.data[column].quantile(0.25)
            Q3 = self.data[column].quantile(0.75)
            IQR = Q3 - Q1
            return self.data[(self.data[column] < (Q1 - 1.5 * IQR)) | (self.data[column] > (Q3 + 1.5 * IQR))]

# Testing with a dataset
# We won't load any files now, but let's ensure the class is defined properly.
DataAnalyzer
