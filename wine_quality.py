import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

wine_data = pd.read_csv(r"C:\Users\ofaru\Desktop\GitHub\Wine_Quality_Analyzing\winequality_data.csv")

print(wine_data.head())
print(wine_data.shape)
print(wine_data.describe())
print(wine_data["quality"].value_counts())
wine_data.rename(columns={
    "fixed acidity" : "Fixed_Acidity", "volatile acidity" : "Volatile_Acidity", "citric acid" : "Citric_Acid", "residual sugar" : "Residual_Sugar", "free sulfur dioxide" : "Free_Sulfur_Dioxide",
    "total sulfur dioxide" : "Total_Sulfur_Dioxide", "chlorides": "Chlorides", "density":"Density", "sulphates":"Sulphates", "alcohol":"Alcohol", "quality":"Quality"
}, inplace= True)

print(wine_data.describe())
print(wine_data.isnull().sum())
dupl_entr_1 = wine_data[wine_data.duplicated()] # find duplicate entries
print("Dupicate Entries: ", dupl_entr_1.shape)
wine_data = wine_data.drop_duplicates() # delete duplicate entries

print(wine_data.corr())

print(wine_data.Quality)

y = wine_data.Quality
x = wine_data.drop("Quality", axis=1)

plt.figure(figsize=(16,12))
sns.heatmap(wine_data.corr(), cmap="bwr", annot= True)

plt.figure(figsize=(12,8))
sns.countplot(x= "Quality", data=wine_data)

#sns.pairplot(wine_data)

plt.figure()
sns.boxplot(data=wine_data, x= wine_data["Quality"], y= wine_data["Alcohol"],palette="GnBu_d")
plt.title("Boxplot Graph of Quality and Alcohol")


wine_data.hist(bins=10, figsize=(16,12))
plt.show()