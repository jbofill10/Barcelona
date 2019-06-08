import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Data\population.csv', delimiter=",")

# Checking for nulls
print(df.isnull().sum().sum())

# Group the total population per year from 2013-2017 (0-4)
population_per_year = df.groupby('Year')['Number'].sum().reset_index()
print(population_per_year)
plt.plot(population_per_year.Year, population_per_year.Number)
plt.show()

