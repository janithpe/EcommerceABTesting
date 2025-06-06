# Importing required libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Reading the data from Data folder and understanding
ab_test = pd.read_csv("Data/ab_test.csv")
ab_test = ab_test.rename(columns={"id":"user_id", "con_treat":"group", "page": "landing_page"})
print(ab_test.head())
print()
print(f"Dataset size: {ab_test.shape}")
print()
print(f"Number of unique users: {ab_test.user_id.nunique()}")
print()
print(ab_test.info())
print()
print(ab_test.isnull().sum())
print()

# Checking duplicate user_ids
print(f"Duplicated user_id found: {ab_test["user_id"].duplicated().any()}")

# Checking the data mismatch
crosstabDF = pd.crosstab(ab_test.group, ab_test.landing_page, margins=True)
print(crosstabDF)

crosstabDF.plot.bar(figsize=(10,5))
plt.grid(axis="y")

mismatch_mask = (
    ((ab_test["group"] == "treatment") & (ab_test["landing_page"] == "old_page")) |
    ((ab_test["group"] == "control") & (ab_test["landing_page"] == "new_page")))
n_mismatch = len(ab_test[mismatch_mask])
print(f"Number of data mismatch: {n_mismatch}")
print(f"Data mismatch percentage: {round(n_mismatch/len(ab_test)*100, 2)}%")

# Removing mismatched rows
ab_test_cleaned = ab_test[~mismatch_mask].copy()

# Checking duplicate user_ids in cleaned dataset
print(f"Duplicated user_id found after removing mismatched rows: {ab_test_cleaned["user_id"].duplicated().any()}")

# Dropping duplicte user_ids, keeping the first occurrence
ab_test_cleaned = ab_test_cleaned.drop_duplicates(subset = "user_id")

# Checking cleaned dataset
print(f"Cleaned dataset shape: {ab_test_cleaned.shape}")
print()
print(ab_test_cleaned["group"].value_counts())
print()
print(ab_test_cleaned.groupby("group")["converted"].mean())
