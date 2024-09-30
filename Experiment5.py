import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data from CSV
def import_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File not found.")
        return None

# Export data to CSV
def export_data(data, file_path):
    try:
        data.to_csv(file_path, index=False)
        print(f"Data exported to {file_path}")
    except Exception as e:
        print(f"Error in exporting: {e}")

# Show details of the dataset (Basic EDA)
def dataset_details(data):
    if data is not None:
        print("\n--- Dataset Overview ---\n")
        print("Number of Rows:", data.shape[0])
        print("Number of Columns:", data.shape[1])
        print("\nFirst five rows:\n", data.head())
        print("\nDataset Size:", data.size)
        print("\nMissing Values in Each Column:\n", data.isnull().sum())
        print("\nData Types of Each Column:\n", data.dtypes)
        
        # Statistical Summary of Numerical Columns
        print("\n--- Statistical Summary of Numerical Columns ---")
        print(data.describe())
        
        # Checking Unique Values in Categorical Columns
        categorical_columns = data.select_dtypes(include=['object']).columns
        print("\n--- Unique Values in Categorical Columns ---")
        for col in categorical_columns:
            print(f"\nColumn '{col}':\n", data[col].value_counts())
        
        return data
    else:
        print("No data to display details.")

# Handling Missing Data (Example: Fill Missing Values)
def handle_missing_data(data):
    print("\n--- Handling Missing Data ---")
    
    # Option 1: Fill missing numeric values with mean
    numeric_data = data.select_dtypes(include=['number'])
    data[numeric_data.columns] = numeric_data.fillna(numeric_data.mean())

    # Option 2: Fill missing categorical values with mode
    categorical_data = data.select_dtypes(include=['object'])
    for col in categorical_data.columns:
        data[col] = data[col].fillna(data[col].mode()[0])
    
    print("\nMissing values handled (filled with mean for numeric and mode for categorical data).")
    return data

# Data Visualization (Correlation Heatmap, Histograms)
def data_visualization(data):
    print("\n--- Data Visualization ---")
    
    # Correlation Matrix Heatmap for Numerical Columns
    plt.figure(figsize=(10, 6))
    sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt='.2f', linewidths=0.5)
    plt.title("Correlation Heatmap")
    plt.show()
    
    # Histograms for Numerical Columns
    data.hist(figsize=(12, 10), bins=20)
    plt.suptitle("Histograms of Numerical Features")
    plt.show()
    
    # Boxplot for Numerical Columns
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=data.select_dtypes(include=['number']), orient="h", palette="Set2")
    plt.title("Boxplot of Numerical Features")
    plt.show()

# Example usage
if __name__ == "__main__":
    # Import the dataset
    file_path = 'input_dataset.csv'  # Replace with your file path
    data = import_data(file_path)

    # Show dataset details
    data = dataset_details(data)

    # Handle missing data (fill missing values)
    data = handle_missing_data(data)

    # Visualize the data
    data_visualization(data)

    # Export the dataset after handling missing values (optional)
    output_file_path = 'output_dataset.csv'  # Replace with your output file path
    export_data(data, output_file_path)
