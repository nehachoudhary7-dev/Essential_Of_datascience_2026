import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')


# 1. First 5 rows
print(data.head())

# 2. Last 5 rows
print(data.tail())

# 3. Shape
print(data.shape)

# 4. Info (print manually captured format)
print(data.info())

# 5. Describe
print(data.describe())

# 6. Missing values
print(data.isnull().sum())

# 7. Fill Age
data['Age'] = data['Age'].fillna(data['Age'].median())

# 8. Fill Embarked
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])

# 9. Drop Cabin
data.drop('Cabin', axis=1, inplace=True)

# 10. FamilySize
data['FamilySize'] = data['SibSp'] + data['Parch']
