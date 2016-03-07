# ----------------
# IMPORT PACKAGES
# ----------------

# The pandas package is used to fetch and store data in a DataFrame.
# The matplotlib package is for graphical outputs (eg. box-plot, histogram, QQ-plot).
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB

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
print("")

# ----------------
# VISUALIZE DATA
# ----------------

# Histogram of raw data in terms of ideal and actual weight
plt.figure()
plt.hist(data["actual"], bins=30, alpha=0.5, label="Actual")
plt.hist(data["ideal"], bins=30, alpha=0.5, label="Ideal")
plt.gca().grid(True)
plt.xlabel("Mass (lbs)", fontsize=14)
plt.ylabel("Count", fontsize=14)
plt.title("Histogram of Ideal and Actual Weight of Participants", fontsize=16)
plt.legend(loc="upper right")
plt.savefig("hist-weights.png")

# Histogram of processed data in terms of difference between ideal and actual weight.
plt.figure()
plt.hist(data["diff"], bins=30, alpha=0.5, label="Actual - Ideal")
plt.gca().grid(True)
plt.xlabel("Mass (lbs)", fontsize=14)
plt.ylabel("Count", fontsize=14)
plt.title("Histogram of Difference between Actual and Ideal Weight of Participants", fontsize=16)
plt.legend(loc="upper right")
plt.savefig("hist-diff.png")

# ----------------
# MODEL DATA
# ----------------

# Assign "sex" or gender as a categorical variable. Female = 0, Male = 1
data["sex"] = pd.Categorical(data["sex"]).labels
data.groupby("sex").describe()

# Partition data into training and testing sets.
partition = int(len(data) * 0.70) # 70% of the data is used as training to model
train = data[:partition]
test = data[partition:]

# Declaration of predictor on training set and use prediction on test set.
train_target = train["sex"]
train_data = train.ix[:,2:]
clf = GaussianNB()
clf.fit(train_data, train_target)

test_target = test["sex"]
test_data = test.ix[:,2:]
predict = clf.predict(test_data)

# ----------------
# TEST DATA
# ----------------

# Verify if model based on training data correctly predicts test data.
count = 0
test_list = list(test_target)
for i in range(len(test_list)):
	if test_list[i] == predict[i]:
		count += 1
print("The model correctly predicted " + str(count) + " from " + str(len(test_list)) + " values.")
print("An accuracy of " + str(float(count / len(test_list) * 100)) +  "%.")
print("")

# Gender prediction with input of actual and ideal weight. Female = 0, Male = 1.
# Actual = 145, Ideal = 160, Difference = -15
print("Testing model with actual weight of 145 and ideal weight of 160 (Female = 0, Male = 1):")
print(clf.predict([[145, 160, -15]])[0])

# Actual = 160, Ideal = 145, Difference = 15
print("Testing model with actual weight of 160 and ideal weight of 145 (Female = 0, Male = 1):")
print(clf.predict([[160, 145, 15]])[0])
print("")

# ----------------
# USER INPUT
# ----------------
mass_act = int(raw_input("Please insert your actual mass in pounds: "))
mass_ide = int(raw_input("Please insert your ideal mass in pounds: "))
mass_diff = mass_act - mass_ide

x = clf.predict([[mass_act, mass_ide, mass_diff]])[0]

if x == 0:
	print("Based on the model your gender is FEMALE.")
else:
	print("Based on the model your gender is MALE.")