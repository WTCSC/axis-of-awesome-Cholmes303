import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("dark_background")

# Reads both csv files and creates dataframes of them.
gdp_df = pd.read_csv("gdp_2015.csv", usecols=["GDP (Billions)"])
happiness_df = pd.read_csv("happiness_2015.csv", usecols=["Country (Happiness Rank)", "Happiness Score"])

fig, ax = plt.subplots(figsize=(50, 10))
# Fits graph to screen for best viewing.
fig.subplots_adjust(left=.045, bottom=.23, right=.98, top=.953)

# Plots countries (ranked 1-50) and GDP for each country. Format is (x,y).
plt.scatter(happiness_df["Country (Happiness Rank)"], gdp_df)
# Makes country names smaller.
ax.tick_params(axis="y", labelsize=8)

plt.rcParams["figure.figsize"] = [10, 10]

# Adds 50 ticks to y axis for a more detailed representation.
plt.locator_params(axis="y", nbins=50)

# Sets y limit to zero.
plt.ylim(0)

# Rotates x-axis labels to be readable.
plt.xticks(rotation=90)

# Title and axes names and sizing. 
plt.title("Comparison: Countries Happiness Score to Normalized GDP", fontsize=20)
plt.xlabel("Countries, Ranked by happiness score", fontsize=14)
plt.ylabel("GDP (Billions of dollars)", fontsize=14)

plt.show()