[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18859768)
# Axis of Awesome

## Overview
This project consists of three Python scripts that visualize the relationship between GDP (Gross Domestic Product) and happiness scores of various countries using different chart types. The data is sourced from CSV files containing GDP and happiness scores, of the top 50 countries, for the year 2015.

## Prerequisites
Ensure you have the following dependencies installed:
- Python 3.x
- pandas
- matplotlib

You can install the required libraries using:
```bash
pip install pandas matplotlib
```

## Data Files
The scripts use the following CSV files:
- `gdp_2015.csv`: Contains GDP data with columns:
  - `Country Name`
  - `GDP (Billions)`
- `happiness_2015.csv`: Contains happiness scores with columns:
  - `Country (Happiness Rank)`
  - `Happiness Score`

Ensure these files are in the same directory as the scripts.

## Scripts
There are three different visualizations that were made for analysis each in their own python file.

### 1. Bar Chart Visualization (`bar_graph.py`)
This script generates a bar graph comparing the GDP of the top 50 happiest countries.
#### Features:
- Uses a dark background theme.
- X-axis: Countries ranked by happiness score.
- Y-axis: GDP (Billions of dollars).
- Rotates x-axis labels for readability.

Run the script:
```bash
python bar_graph.py
```

![Bar Graph][205217.png]

### 2. Line Chart Visualization (`line_graph.py`)
This script plots a line graph to show the relationship between happiness ranking and GDP.
#### Features:
- Uses `plot()` to display the trend.
- X-axis: Country names sorted by happiness rank.
- Y-axis: GDP values.
- Rotates x-axis labels for readability.

Run the script:
```bash
python line_graph.py
```

![Line Graph][205244.png]

### 3. Scatter Plot Visualization (`scatter_plot.py`)
This script creates a scatter plot to show the correlation between happiness ranking and GDP.
#### Features:
- Uses `scatter()` to plot data points.
- X-axis: Country names sorted by happiness rank.
- Y-axis: GDP values.
- Rotates x-axis labels for readability.

Run the script:
```bash
python scatter_plot.py
```

![Scatter Plot][205315.png]

## Notes
- The scripts assume that the data files contain the correct column names.
- Adjust `figsize` or `subplots_adjust` as needed for better visualization on different screens.
- Modify the file paths if necessary to match your data directory structure.

[def]: fd