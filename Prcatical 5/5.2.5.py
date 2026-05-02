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

# Write your code here for Bar Plot for Survival by Pclass

# Bar Plot for Survival by Pclass

# Group by 'Pclass' and count survival values using value_counts()
survival_pclass = data.groupby('Pclass')['Survived'].value_counts().unstack(fill_value=0)

# Plot stacked bar chart
survival_pclass.plot(kind='bar', stacked=True)

# Add title and labels
plt.title("Survival by Pclass")
plt.xlabel("Pclass")
plt.ylabel("Count")

# Add legend
plt.legend(['Not Survived', 'Survived'])

# Show the plot
plt.show()
