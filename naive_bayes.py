# ----------------
# IMPORT PACKAGES
# ----------------

# The pandas package is used to fetch and store data in a DataFrame.
import pandas as pd

# ----------------
# OBTAIN DATA
# ----------------

# Data Source: https://www.dropbox.com/s/hg0tqy6saqeoq0j/ideal_weight.csv?dl=0

# ----------------
# PROFILE DATA
# ----------------

# Determine number of observations or data points in the data set.
data = pd.read_csv("ideal_weight.csv")
col = [i.replace("'", "") for i in data.columns]
data.columns = col
col_gender = [i.replace("'", "") for i in data["sex"]]
data["sex"] = col_gender

observations = len(data)
num_col = len(data.columns)
print("Number of Observations: " + str(observations))
print("Number of Columns: " + str(num_col))