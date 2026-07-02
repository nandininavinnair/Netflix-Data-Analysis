import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
df = pd.read_csv("netflix_titles.csv")

# Display the first 5 rows
print(df.head())

# the shape of the dataset
print("\nShape of the dataset:")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns)

# Information about the dataset
print("\nDataset Information:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())


# Remove duplicate rows (if any)
df.drop_duplicates(inplace=True)

# Fill missing values
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Unknown', inplace=True)
df['country'].fillna('Unknown', inplace=True)
df['rating'].fillna('Not Rated', inplace=True)

# Remove rows with missing date_added or duration
df.dropna(subset=['date_added', 'duration'], inplace=True)

# Check if there are still missing values
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nMovies and TV Shows Count:")
print(df['type'].value_counts())

# Plot Movies vs TV Shows
plt.figure(figsize=(6,4))
sns.countplot(x='type', data=df)

plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")

plt.show()







# Top 10 countries with the most Netflix content

top_countries = df['country'].value_counts().head(10)

print("\nTop 10 Countries:")
print(top_countries)

plt.figure(figsize=(10,5))
sns.barplot(x=top_countries.index, y=top_countries.values)

plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)

plt.show()