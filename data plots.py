import pandas as pd
import matplotlib.pyplot as plt

#Histogram
data = pd.read_csv('C:\\Users\\PC\\Desktop\\class\\CS7265\\hw1\\Book1.csv')
data.loc[data['OS_STATUS'] == "DECEASED", "AGE"].value_counts().sort_index()
data['AGE'].hist()
plt.show()

#Make a scatter plot that shows the correlation between “AGE” and “OS_MONTHS”
#this method is incomplete
data = pd.read_csv('C:\\Users\\farid-PC\\Desktop\\class\\CS7265_BIG_DATA\\hw1\\Book1.CSV')
#data.loc[data['OS_STATUS'] == "DECEASED", "AGE"].value_counts().sort_index()
fig, ax = plt.subplots()
scatter_plot = ax.scatter(
    data['AGE'], data['OS_MONTHS']
)
plt.show()

