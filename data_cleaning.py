import pandas as pd

# Load dataset
df = pd.read_csv("Mall_Customers.xlsx.csv")

# Dataset shape
print("Shape:", df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicates
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Rename columns
df.columns = (
    df.columns
      .str.lower()
      .str.replace(" ", "_")
      .str.replace("(", "", regex=False)
      .str.replace(")", "", regex=False)
)

# Standardize gender values
df["gender"] = df["gender"].str.strip().str.title()

# Check data types
print("\nData Types:")
print(df.dtypes)

# Save cleaned dataset
df.to_csv("Mall_Customers_Cleaned.csv", index=False)

print("\nData Cleaning Completed Successfully!")