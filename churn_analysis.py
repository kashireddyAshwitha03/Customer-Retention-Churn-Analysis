import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/customer_data.csv")

print(df.head())

churn_rate = df['Churn'].value_counts(normalize=True) * 100

print("\nChurn Rate:")
print(churn_rate)

churn_rate.plot(kind='bar')
plt.title("Customer Churn Analysis")
plt.xlabel("Churn")
plt.ylabel("Percentage")
plt.show()