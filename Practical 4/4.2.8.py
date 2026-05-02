import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)


print(data[data['Survived'] == 1]['Sex'].value_counts())

# 2. Number of non-survivors by gender
print(data[data['Survived'] == 0]['Sex'].value_counts())

# 3. Number of survivors by embarked location (Embarked_S)
print(data[data['Survived'] == 1]['Embarked_S'].value_counts())

# 4. Number of non-survivors by embarked location (Embarked_S)
print(data[data['Survived'] == 0]['Embarked_S'].value_counts())

# 5. Percentage of children (Age < 18) who survived
children = data[data['Age'] < 18]
print(children['Survived'].mean())

# 6. Percentage of adults (Age >= 18) who survived
adults = data[data['Age'] >= 18]
print(adults['Survived'].mean())

# 7. Median age of survivors
print(data[data['Survived'] == 1]['Age'].median())

# 8. Median age of non-survivors
print(data[data['Survived'] == 0]['Age'].median())

# 9. Median fare of survivors
print(data[data['Survived'] == 1]['Fare'].median())

# 10. Median fare of non-survivors
print(data[data['Survived'] == 0]['Fare'].median())
