import pandas as pd

# Load the CSV files
keywords_everywhere_df = pd.read_csv(
    "keywords-everywhere-exported.csv", usecols=["Keyword", "Search Volume (Global)"]
)
moz_df = pd.read_csv("moz-exported.csv", usecols=["Keyword", "Difficulty"])

# Rename columns for easier handling
keywords_everywhere_df.rename(
    columns={"Search Volume (Global)": "Search Vol"}, inplace=True
)

# Merge the dataframes on 'Keyword', using an inner join to automatically exclude keywords without a difficulty score
final_df = pd.merge(keywords_everywhere_df, moz_df, on="Keyword", how="inner")

# If a keyword's search volume is not found, the cell should be left empty,
# pandas automatically handles this during the merge operation if there are missing values.

# Write the result to a new CSV file, overwriting if it already exists
final_df.to_csv("final-keywords.csv", index=False)

print("CSV file 'final-keywords.csv' has been created successfully.")
