
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("customer_churn.csv")

# Display first five rows
print("First Five Rows:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].mean())

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Check duplicate values
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Churn count visualization
if 'Churn' in df.columns:
    sns.countplot(x='Churn', data=df)
    plt.title("Customer Churn Count")
    plt.show()

# Histogram
df.select_dtypes(include=np.number).hist(figsize=(10, 8))
plt.suptitle("Numerical Data Distribution")
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.select_dtypes(include=np.number).corr(),
            annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Boxplot for outlier detection
num_cols = df.select_dtypes(include=np.number).columns

for col in num_cols:
    sns.boxplot(x=df[col])
    plt.title("Outlier Detection: " + col)
    plt.show()

# Handle outliers using IQR
for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df[col] = df[col].clip(lower, upper)

print("\nCleaned Dataset:")
print(df.head())

print("\nEDA Completed Successfully!")
