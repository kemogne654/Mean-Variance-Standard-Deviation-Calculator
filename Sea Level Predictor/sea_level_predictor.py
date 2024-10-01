import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Load the dataset
    df = pd.read_csv('epa-sea-level.csv')

    # Create a scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # Create a line of best fit using all data
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))  # Extend to 2050
    plt.plot(years_extended, slope * years_extended + intercept, color='red', label='Best Fit Line (1880-2050)')

    # Create a line of best fit using data from year 2000 onwards
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    plt.plot(years_extended, slope_2000 * years_extended + intercept_2000, color='green', label='Best Fit Line (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid()

    # Save the figure
    plt.savefig('sea_level_plot.png')
    plt.show()  # Display the plot

# Uncomment the following lines to run the function
if __name__ == "__main__":
    draw_plot()
