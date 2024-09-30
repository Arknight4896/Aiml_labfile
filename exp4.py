import pandas as pd

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

# Show details of the dataset
def dataset_details(data):
    if data is not None:
        print("Number of Rows:", data.shape[0])
        print("Number of Columns:", data.shape[1])
        print("\nFirst five rows:\n", data.head())
        print("\nDataset Size:", data.size)
        print("\nMissing Values in Each Column:\n", data.isnull().sum())

        # Numerical columns
        numeric_data = data.select_dtypes(include=['number'])
        
        print("\nSum of Numerical Columns:\n", numeric_data.sum())
        print("\nAverage of Numerical Columns:\n", numeric_data.mean())
        print("\nMinimum Values of Numerical Columns:\n", numeric_data.min())
        print("\nMaximum Values of Numerical Columns:\n", numeric_data.max())
    else:
        print("No data to display details.")

# Example usage
if __name__ == "__main__":
    # Import the dataset
    file_path = 'input_dataset.csv'  # Replace with your file path
    data = import_data(file_path)

    # Show dataset details
    dataset_details(data)

    # Export the dataset (optional)
    output_file_path = 'output_dataset.csv'  # Replace with your output file path
    export_data(data, output_file_path)
