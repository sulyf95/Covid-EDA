# Importing all the packages I will be using in this  project

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Loading and inspecting the dataset, with .shape, .drop and .head()

corona_dataset = pd.read_csv("covid19_Confirmed_dataset.csv")
corona_dataset.head()
corona_dataset.shape
corona_dataset.drop(["Lat","Long"],axis = 1, inplace = True)
corona_dataset.head(10)
corona_dataset_aggregated = corona_dataset.groupby("Country/Region").sum()
corona_dataset_aggregated.head()
corona_dataset_aggregated.shape

# Visualising the covid data for a few countries using the .loc method

corona_dataset_aggregated.loc["China"].plot()
corona_dataset_aggregated.loc["Italy"].plot()
corona_dataset_aggregated.loc["Spain"].plot()
corona_dataset_aggregated.loc["United Kingdom"].plot()
plt.legend()

# Plotting a graph of the UK overall confirmed cases since patient zero

corona_dataset_aggregated.loc["United Kingdom"].plot(color="red")
plt.title("UK Confirmed Covid Cases")
plt.xlabel("Date")
plt.ylabel("Number Of Cases")

# Looking at the first significant covid wave in the UK

corona_dataset_aggregated.loc["United Kingdom"][35:50].plot(color="red")
plt.title("First Wave Of Covid Cases UK")
plt.xlabel("Date")
plt.ylabel("Number Of Cases")

# Calculating the rate of change using the derivatives function

corona_dataset_aggregated.loc["United Kingdom"].diff().plot(color="red")
plt.title("UK Infection Rate per Day")
plt.xlabel("Date")
plt.ylabel("Number Of Cases")

# Finding the maximum single day covid confirmed cases for each country

corona_dataset_aggregated.loc["United Kingdom"].diff().max()
corona_dataset_aggregated.loc["China"].diff().max()
corona_dataset_aggregated.loc["Italy"].diff().max()
corona_dataset_aggregated.loc["Spain"].diff().max()

# Finding the peak infection rate of each country and putting it into a dataframe

countries = list(corona_dataset_aggregated.index) 
max_infection_rates = [] 
for c in countries:
    max_infection_rates.append(corona_dataset_aggregated.loc[c].diff().max())  
corona_dataset_aggregated["max_infection_rate"] = max_infection_rates 
corona_dataset_aggregated.head()
corona_data = pd.DataFrame(corona_dataset_aggregated["max_infection_rate"])
corona_data.head(20)

# Import the dataset

world_happiness_report = pd.read_csv("worldwide_happiness_report.csv")
world_happiness_report.head()
world_happiness_report.shape

# Remove unnecessary coloumns from the data

useless_cols = ["Overall rank", "Score", "Generosity","Perceptions of corruption"]
world_happiness_report.drop(useless_cols, axis=1, inplace = True)
world_happiness_report.head()
world_happiness_report.set_index(["Country or region"],inplace = True)
world_happiness_report.head()

# Join the tables using the inner function

data = corona_data.join(world_happiness_report, how = "inner")
data.head()

# A correlation analysis between two coloumns of the dataset
data.corr()

# Correlation between maximum infection rate with GDP, social support, life expectancy and democracy

x_axis = data["GDP per capita"]
y_axis = data["max_infection_rate"]
sns.scatterplot(x_axis, np.log(y_axis))
sns.regplot(x_axis, np.log(y_axis))


x = data["Social support"]
y = data["max_infection_rate"]
sns.scatterplot(x, np.log(y))
sns.regplot(x, np.log(y))


x = data["Healthy life expectancy"]
y = data["max_infection_rate"]
sns.scatterplot(x, np.log(y))
sns.regplot(x, np.log(y))


x = data["Freedom to make life choices"]
y = data["max_infection_rate"]
sns.scatterplot(x, np.log(y))
sns.regplot(x, np.log(y))