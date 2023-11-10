"""
ADS-1 Assignment 1: Visualisation

Author: Md Nadimozzaman Pappo <mnpappo@gmail.com>
Date: 02-11-2023
Used Python Version: 3.11.4
Format: Black
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data: SARC Country Population
# Source: Wordl Bank
# URL: https://data.worldbank.org/indicator/SP.POP.TOTL?end=2022&locations=BD-IN-PK-NP-AF-MV-BT-LK&name_desc=false&start=1960&view=chart

# Read the data from csv file
data = pd.read_csv("./data/population.csv")
# select the data for SARC countries
data = data.loc[
    data["Country Name"].isin(
        ["Bangladesh", "India", "Pakistan", "Nepal", "Bhutan", "Sri Lanka", "Maldives"]
    )
]


def line_plot(data, start_year, interval=5):
    """
    Create a line plot for Population Values over time.

    Parameters:
    - data: Pandas DataFrame containing the dataset.
    - start_year: The starting year for visualization.
    - interval: The interval between selected years (default is 5).

    Returns:
    None (displays the plot).
    """
    # Extract relevant columns for plotting
    years_selected = [
        col
        for col in data.columns[4:]
        if col.isdigit()
        and int(col) >= start_year
        and (int(col) - start_year) % interval == 0
    ]

    # Plotting
    plt.figure(figsize=(10, 6))

    # Plot a line for each country
    for index, row in data.iterrows():
        country_name = row["Country Name"]
        plt.plot(years_selected, row[years_selected], label=country_name)

    plt.xlabel("Year")
    plt.ylabel("Population Value (Billions)")
    plt.title(
        f"Line Plot of Population Values Over Time (Start Year: {start_year}, Interval: {interval} Years)"
    )
    plt.legend()
    plt.grid(True)
    plt.show()


# Use the line_plot function
line_plot(data, start_year=1960, interval=5)


def bar_chart(data, year):
    """
    Create a bar chart for Population Values at a specific year.

    Parameters:
    - data: Pandas DataFrame containing the dataset.
    - year: The specific year for visualization.

    Returns:
    None (displays the plot).
    """
    # Extract relevant columns for plotting
    indicator_values = data[str(year)]

    # Plotting
    plt.figure(figsize=(10, 6))

    # Create a bar for each country
    plt.bar(data["Country Name"], indicator_values)

    plt.xlabel("Country")
    plt.ylabel("Population Value (Billions)")
    plt.title(f"Bar Chart of Population Values in {year}")
    plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for better readability
    plt.grid(axis="y")
    plt.show()


# Use the bar_chart function
bar_chart(data, year=2020)


def pie_chart(data, country_names):
    """
    Create a pie chart for the Population Values of multiple countries.

    Parameters:
    - data: Pandas DataFrame containing the dataset.
    - country_names: List of country names for visualization.

    Returns:
    None (displays the plot).
    """
    # Extract relevant data for the specified countries
    countries_data = data[data["Country Name"].isin(country_names)]

    # Select columns containing Population Values
    indicator_columns = countries_data.columns[4:]

    # Convert Population Values from billions to millions
    indicator_values = countries_data[indicator_columns] * 1000

    # Sum Population Values across the years
    total_values = indicator_values.sum(axis=1)

    # Plotting
    plt.figure(figsize=(8, 8))

    # Create a pie chart
    plt.pie(
        total_values,
        labels=countries_data["Country Name"],
        autopct="%1.1f%%",
        startangle=90,
    )

    plt.title("Pie Chart of Population Values (Millions) for SARC Countries")
    plt.show()


# Specify the list of countries for the pie chart
sarc_countries_countries = [
    "Bangladesh",
    "India",
    "Pakistan",
    "Nepal",
    "Bhutan",
    "Sri Lanka",
    "Maldives",
]

# Use the pie_chart function
pie_chart(data, country_names=sarc_countries_countries)
