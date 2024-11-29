import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def combine_csv_files(input_folder, output_file):
    """
    Combines multiple CSV files in a folder into a single CSV file.

    Parameters:
    - input_folder: str, folder path containing the CSV files.
    - output_file: str, path to save the combined CSV file.
    """
    try:
        # List to hold dataframes
        all_data = []
        
        # Iterate through CSV files in the folder
        for filename in os.listdir(input_folder):
            if filename.endswith('.csv'):
                file_path = os.path.join(input_folder, filename)
                print(f"Processing file: {file_path}")
                
                # Read CSV into a DataFrame
                df = pd.read_csv(file_path)
                all_data.append(df)
        
        # Combine all dataframes into one
        combined_df = pd.concat(all_data, ignore_index=True)
        
        # Save the combined DataFrame to a CSV
        combined_df.to_csv(output_file, index=False)
        print(f"Combined CSV saved to {output_file}")
        
        return combined_df
    
    except Exception as e:
        print(f"Error occurred: {e}")

# Example usage:
input_folder = "/Users/declansaul/Documents/Programming/NASA-HAB-Mission/data"

output_file = "combinedData.csv"               # Replace with your desired output file path

combined_data = combine_csv_files(input_folder, output_file)

# Optionally, perform a simple visualization to confirm data integrity
if not combined_data.empty:
    print("Preview of combined data:")
    print(combined_data.head())
    
    # Example: Plot a histogram of a numeric column if it exists
    numeric_columns = combined_data.select_dtypes(include=np.number).columns
    if len(numeric_columns) > 0:
        plt.figure(figsize=(8, 6))
        combined_data[numeric_columns[0]].hist(bins=30, color='skyblue', edgecolor='black')
        plt.title(f"Distribution of {numeric_columns[0]}")
        plt.xlabel(numeric_columns[0])
        plt.ylabel("Frequency")
        plt.show()
    else:
        print("No numeric columns to plot.")
else:
    print("No data to visualize.")
