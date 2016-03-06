# ----------------
# IMPORT PACKAGES
# ----------------

# The pandas package is used to fetch and store data in a DataFrame.
# The matplotlib package is for graphical outputs (eg. box-plot, histogram, QQ-plot).
import pandas as pd
import matplotlib.pyplot as plt

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

# ----------------
# VISUALIZE DATA
# ----------------
plt.hist(data["actual"], bins=30, alpha=0.5, label="Actual")
plt.hist(data["ideal"], bins=30, alpha=0.5, label="Ideal")
plt.gca().grid(True)
plt.xlabel("Mass (lbs)", fontsize=14)
plt.ylabel("Count", fontsize=14)
plt.title("Histogram of Ideal and Actual Weight of Participants", fontsize=16)
plt.legend(loc="upper right")
plt.show()