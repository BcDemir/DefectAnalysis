import pandas as pd
import numpy as np


df = pd.read_csv('data/defects_data.csv')

print(df.info())
print(df['defect_date'].head())


print(df['severity'].nunique())

# Convert the date column
df['defect_date'] = pd.to_datetime(df['defect_date'], errors='coerce')

# Check for columns that are not date
print('*****Incorrect date*****')
print(df[df['defect_date'].isna()])
print('*****Incorrect date*****')

print(df['defect_date'].head(), '\n')


# --- Extract year, month, and weekday ---
df['year'] = df['defect_date'].dt.year
df['month'] = df['defect_date'].dt.month
df['weekday'] = df['defect_date'].dt.day

# Check for duplicates - There is none
duplicates = df[df.duplicated()]
print(duplicates, '\n')


# --- Optional: check for missing values ---
print("Missing values per column:")
print(df.isnull().sum(), '\n')


# --- Convert categorical columns ---
df['defect_type'] = df['defect_type'].astype('category')
df['defect_location'] = df['defect_location'].astype('category')
df['inspection_method'] = df['inspection_method'].astype('category')

# --- For severity, define an ORDERED category ---
df['severity'] = pd.Categorical(df['severity'], ordered=True)

# --- Save updated dataset ---
df.to_csv("cleaned/defects_data_categorized.csv", index=False)
print("\n Categorical conversion complete! Saved as 'defects_data_categorized.csv'")