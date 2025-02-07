import pandas as pd

def preprocess_csv(input_file, output_file, columns_to_modify):
    # Load CSV file
    df = pd.read_csv(input_file, dtype=str)  # Read all data as string to prevent type issues

    # Replace spaces with Zero Width Non-Joiner (\u200C) in specified columns
    for col in columns_to_modify:
        if col in df.columns:  # Check if column exists
            df[col] = df[col].str.replace(" ", "\u00A0", regex=False)

    # Save processed file
    df.to_csv(output_file, index=False, encoding='utf-8')

    print(f"Processed file saved as: {output_file}")

# Example usage
input_csv = "_data/comic-book-paratexts-metadata_spaces.csv"   # Replace with your input file name
output_csv = "_data/comic-book-paratexts-metadata.csv"  # Replace with your desired output file name
columns = ["tag", "paratext_type", "publisher"]  # Replace with the columns you want to modify

preprocess_csv(input_csv, output_csv, columns)
