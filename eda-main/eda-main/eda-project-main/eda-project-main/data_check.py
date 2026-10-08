import pandas as pd

df = pd.read_csv("student_performance.csv")

print("Shape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
print("\nStatistical summary:\n", df.describe().round(2))
print("\nCorrelation with Final Score:\n",
      df.select_dtypes("number").corr()["Final_Score"].sort_values(ascending=False))
