# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import os

# Set seaborn style for better visuals
sns.set_style("whitegrid")

# Task 1: Load and Explore the Dataset
try:
    # Load Iris dataset (simulating CSV loading)
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    
    # Display first few rows
    print("First 5 Rows of the Dataset:")
    print(df.head())
    
    # Check data types and structure
    print("\nDataset Info:")
    print(df.info())
    
    # Check for missing values
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    # Clean dataset: Fill missing values with mean for numerical columns (if any)
    for column in df.select_dtypes(include=['float64']).columns:
        if df[column].isnull().any():
            df[column].fillna(df[column].mean(), inplace=True)
            print(f"Filled missing values in {column} with mean.")
    
    # If no missing values, confirm
    if not df.isnull().any().any():
        print("No missing values found in the dataset.")

except FileNotFoundError:
    print("Error: Dataset file not found. Please ensure the file exists.")
except Exception as e:
    print(f"Error during data loading: {e}")

# Task 2: Basic Data Analysis
try:
    # Compute basic statistics
    print("\nSummary Statistics:")
    print(df.describe())
    
    # Group by species and calculate mean for numerical columns
    print("\nMean Values by Species:")
    group_means = df.groupby('species').mean()
    print(group_means)
    
    # Findings from analysis
    print("\nFindings from Analysis:")
    print("- The dataset has 150 records, 4 numerical columns, and 1 categorical column (species).")
    print("- Setosa has the smallest average petal length (1.46 cm), while virginica has the largest (5.55 cm).")
    print("- Sepal width varies less (std ≈ 0.43 cm) compared to petal length (std ≈ 1.77 cm).")
    print("- Virginica tends to have larger measurements overall, suggesting size as a distinguishing factor.")

except Exception as e:
    print(f"Error during analysis: {e}")

# Task 3: Data Visualization
try:
    # Visualization 1: Line Chart (Simulated trend: Mean sepal length by species index)
    plt.figure(figsize=(8, 6))
    for species in df['species'].unique():
        subset = df[df['species'] == species]
        plt.plot(range(len(subset)), subset['sepal length (cm)'], 
                 label=species, marker='o')
    plt.title('Sepal Length Trend Across Species (Indexed)')
    plt.xlabel('Sample Index')
    plt.ylabel('Sepal Length (cm)')
    plt.legend()
    plt.savefig('sepal_length_line.png')
    plt.close()
    
    # Visualization 2: Bar Chart (Average petal length by species)
    plt.figure(figsize=(8, 6))
    sns.barplot(x='species', y='petal length (cm)', data=df, errorbar=None)
    plt.title('Average Petal Length by Species')
    plt.xlabel('Species')
    plt.ylabel('Petal Length (cm)')
    plt.savefig('petal_length_bar.png')
    plt.close()
    
    # Visualization 3: Histogram (Distribution of sepal width)
    plt.figure(figsize=(8, 6))
    sns.histplot(df['sepal width (cm)'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribution of Sepal Width')
    plt.xlabel('Sepal Width (cm)')
    plt.ylabel('Frequency')
    plt.savefig('sepal_width_histogram.png')
    plt.close()
    
    # Visualization 4: Scatter Plot (Sepal length vs. petal length)
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', 
                    hue='species', style='species', data=df, s=100)
    plt.title('Sepal Length vs. Petal Length by Species')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend(title='Species')
    plt.savefig('sepal_petal_scatter.png')
    plt.close()
    
    print("\nVisualizations saved as PNG files:")
    print("- sepal_length_line.png")
    print("- petal_length_bar.png")
    print("- sepal_width_histogram.png")
    print("- sepal_petal_scatter.png")

except Exception as e:
    print(f"Error during visualization: {e}")