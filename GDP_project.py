# GDP Project: Top 10 Economies by Nominal GDP
# Description: Extracts top 10 countries by nominal GDP from Wikipedia, processes the data, and saves it as CSV.

import pandas as pd
import numpy as np
import requests

# Step 1: Wikipedia URL and request headers
URL = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0 Safari/537.36"
}

# Step 2: Send HTTP GET request
response = requests.get(URL, headers=headers)

# Step 3: Read all HTML tables
tables = pd.read_html(response.text)

# Step 4: Select the table with country names and GDP
gdp_table = tables[2]  # Adjust index if Wikipedia page changes

# Step 5: Clean column headers
gdp_table.columns = range(gdp_table.shape[1])

# Step 6: Select Country and GDP columns
gdp_df = gdp_table[[0, 1]]

# Step 7: Keep top 10 countries
gdp_df = gdp_df.iloc[1:11, :]

# Step 8: Rename columns
gdp_df.columns = ['Country', 'GDP (Million USD)']

# Step 9: Convert Million USD to Billion USD
gdp_df['GDP (Million USD)'] = gdp_df['GDP (Million USD)'].astype(int)
gdp_df['GDP (Billion USD)'] = np.round(gdp_df['GDP (Million USD)'] / 1000, 2)

# Step 10: Drop Million USD column
gdp_df = gdp_df.drop(columns=['GDP (Million USD)'])

# Step 11: Save to CSV
gdp_df.to_csv('Largest_economies.csv', index=False)

# Step 12: Print confirmation and display DataFrame
print("Project completed! Check 'Largest_economies.csv'.")
print(gdp_df)



