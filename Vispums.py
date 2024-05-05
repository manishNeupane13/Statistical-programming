# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
from matplotlib.colors import LinearSegmentedColormap




#method to print assignment information
def print_assignment_information(assignment_number):
    print(
f"""
DATA 5100 - [1st Semester] [2024]
NAME: Manish Neupane
PROGRAMMING ASSIGNMENT {assignment_number}



""")
        

# Set the file path for the CSV file
path = "ss13hil.csv"

# Read the CSV file into a Pandas DataFrame
hill_df = pd.read_csv(path)

# Define a function to map income brackets to numeric values
def get_numeric(data_series):
    # Define brackets and their corresponding numeric values
    data_bracket = {
        1: [0, 0], 2: [0, 1], 22: [0, 50], 62: [1000, 100], 64: [5000, 500], 68: [6000, 1000]
    }
    keys = list(data_bracket.keys())
    # Iterate over income brackets
    for index in range(len(keys)):
        # Check if the data_series is null
        if pd.isnull(data_series):
            return None
        # If the data_series value falls within an bracket, map it to a numeric value
        if data_series <= keys[index]:
            return data_bracket[keys[index]][0] + ((data_series - keys[index - 1]) * data_bracket[keys[index]][1])

# Define a function to plot a pie chart showing household languages
def plot_household_langauge_pie_chart(ax):
    # Dictionary mapping language codes to language names
    language_dict = {
        1: 'English only', 2: 'Spanish', 3: 'Other Indo-European languages',
        4: 'Asian and Pacific Island languages', 5: 'Other language'
    }
    # Group by household language and count occurrences
    house_hold_langugae_count = hill_df.groupby('HHL')['HHL'].value_counts().values
    # Plot pie chart
    wedges, texts = ax.pie(house_hold_langugae_count, startangle=240)
    # Add legend
    ax.legend(wedges, language_dict.values(), title='Pie Chart', loc='right', bbox_to_anchor=(0.5, 0.8))
    # Set title
    ax.set_title("Household Languages")
    # Equal aspect ratio ensures that pie is drawn as a circle
    ax.axis('equal')

# Define a function to plot a histogram showing household income distribution
def plot_income_histogram(ax):
    # Remove null values and ensure all values are positive
    household_income = (hill_df['HINCP'].dropna()).abs()
    # Generate log-spaced bins for the histogram
    bins = np.logspace(1, 7, num=100)
    # Create the histogram with log-spaced bins
    counts, bins, _ = ax.hist(household_income, bins=bins, density=True, alpha=0.5, color='green', label='Histogram')
    # Set x-axis scale to logarithmic
    ax.set_xscale('log')
    # Set y-axis scale and ticks
    ax.set_ylim(0.000000, 0.000025)
    y_axis_label = ['0.000000', '0.000005', '0.000010', '0.000015', '0.000020']
    ax.set_yticks(np.arange(0.000000, 0.000021, 0.000005), y_axis_label)
    # Compute and plot the Kernel Density Estimate (KDE)
    kde = gaussian_kde(household_income)
    kde_vals = kde(bins)
    ax.plot(bins, kde_vals, color='black', linestyle='--', linewidth=2)
    # Set labels and title
    ax.grid(True)
    ax.set_xlabel('Household Income ($) - Log Scaled ')
    ax.set_ylabel('Density')
    ax.set_title('Distribution of Household Income')

# Define a function to plot a bar graph showing the number of vehicles available in households
def plot_vehicle_bar_graph(ax1):
    # Remove null values
    hill_df['VEH'] = hill_df['VEH'].dropna()
    # Calculate vehicle count
    vehicle_count = hill_df.groupby('VEH')['WGTP'].sum() / 1000
    # Plot bar graph
    ax1.bar(vehicle_count.index, vehicle_count.values, color='red')
    # Set labels and title
    ax1.set_xlabel('# of Vehicle')
    ax1.set_ylabel('Thousand of Household')
    ax1.set_title('Vehicle available in Households')

# Define a function to plot a scatter plot showing property taxes vs property values
def plot_tax_vs_valaue_scatter_plot(ax1):
    # Drop null values
    hill_df['TAXP_numeric'] = hill_df['TAXP'].apply(get_numeric)
    hill_df['MRGP Cleaned'] = hill_df['MRGP'].dropna()
    
    # Define custom colormap colors
    colors=[(1/255,1/255,255/255),(0.87,0.87,0.99),(250/250, 190/250, 163/200)]
    # Create custom colormap
    custom_cmap = LinearSegmentedColormap.from_list('custom_cmap', colors, N=150)
    # Scatter plot
    scatter = ax1.scatter(hill_df['VALP'], hill_df['TAXP_numeric'], s=hill_df['WGTP'], c=hill_df['MRGP'],
                          cmap=custom_cmap, marker='o')
    # Colorbar
    cbar = plt.colorbar(scatter)
    cbar.set_label('First Mortage Payment (Monthly $)')
    cbar.ax.yaxis.grid(True, linestyle='--', color='white', alpha=0.5)
    # Set x-axis and y-axis limits to start from 0
    ax1.set_xlim(left=0)
    ax1.set_ylim(bottom=0)
    # Set labels and title
    x_axis_label = np.arange(00000, 1200000 + 1, 200000)
    ax1.set_xticks(x_axis_label, x_axis_label)
    ax1.set_yticks(np.arange(000, 12000, 2000))
    ax1.set_xlabel('Property Value ($)')
    ax1.set_ylabel('Taxes ($)')
    ax1.set_title('Property Taxes vs Property Values')

# Create a figure with larger size
fig = plt.figure(figsize=(25, 12))

# Define the size for each axis
ax1 = fig.add_subplot(221)  # 2x2 grid, 1st subplot
ax2 = fig.add_subplot(222)  # 2x2 grid, 2nd subplot
ax3 = fig.add_subplot(223)  # 2x2 grid, 3rd subplot
ax4 = fig.add_subplot(224)  # 2x2 grid, 4th subplot

# Call your plotting functions for each axis
plot_household_langauge_pie_chart(ax1)
plot_income_histogram(ax2)
plot_vehicle_bar_graph(ax3)
plot_tax_vs_valaue_scatter_plot(ax4)

# Adjust subplot spacing
plt.subplots_adjust(hspace=0.5)

# Automatically adjust subplot parameters
plt.tight_layout()

#assignment information

print_assignment_information(6)
# Show the plot
plt.show()

# Save the plot as an image file
fig.savefig("pums.png")
