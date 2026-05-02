import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')

# Data Cleaning
data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop('Cabin', axis=1, inplace=True)

# Convert categorical features to numeric
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# Write your code here for Bar Plot for Survival by Gender


# Bar Plot for Survival by Gender

# Group by 'Sex' and count survival values
survival_gender = data.groupby('Sex')['Survived'].value_counts().unstack()

# Plot stacked bar chart
survival_gender.plot(kind='bar', stacked=True)

# Add title and labels
plt.title("Survival by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")

# Add legend
plt.legend(['Not Survived', 'Survived'])

# Show the plot
plt.show()
