
import pandas as pd

# Define the file path
path = 'ss13hil.csv'

# Read the CSV file into a DataFrame
hill_df = pd.read_csv(path)


#method to print assignment information
def print_assignment_information(assignment_number):
    print(
f"""
DATA 5100 - [1st Semester] [2024]
NAME: Manish Neupane
PROGRAMMING ASSIGNMENT #{assignment_number}
""")

# Function to categorize household income by household type
def household_income_by_HHT():
    # Dictionary mapping HHT values to household types
    HHT_index = { 
        1.0: "Married couple household",
        2.0: "Other family household: Male householder, no wife present",
        3.0: "Other family household: Female householder, no husband present",
        4.0: "Nonfamily household: Male householder: Living alone",
        5.0: "Nonfamily household: Male householder: Not living alone",
        6.0: "Nonfamily household: Female householder: Living alone",
        7.0: "Nonfamily household: Female householder: Not living alone"
    }
    # Create a new column 'HHT - Household/family type' in 'hill_df' based on 'HHT' values.
    # Use the 'apply' method to map 'HHT' values to descriptions from 'HHT_index' dictionary.
    # If 'HHT' value is not null, assign the corresponding description; otherwise, assign None.

    hill_df['HHT - Household/family type'] = hill_df['HHT'].apply(lambda data_series: HHT_index.get(data_series, None) if pd.notnull(data_series) else None)
    
    # Group by household type and calculate mean, std, count, min, max for household income
   
    result = hill_df.groupby('HHT - Household/family type')['HINCP'].agg(
        mean='mean',
        std='std',
        count='count',
        min='min',
        max='max'
    ) 
    # Sort and return the DataFrame 'result' by the values in the 'mean' column in descending order
    return (result.sort_values(by='mean',ascending=False))


# Function to analyze household language vs. internet access
def houehold_language_vs_access():
    # Dictionary mapping household language and internet access codes to their respective descriptions
    household_language = {
        1: "English only",
        2: "Spanish",
        3: "Other Indo-European languages",
        4: "Asian and Pacific Island languages",
        5: "Other language"
    }
    internet_access = {
        1: "Yes, W/ Subsrc. ",
        2: "Yes, Wo/ Subsrc. ",
        3: "No "
    }
    
    # Select relevant columns and drop rows with missing values
    dummy_df = hill_df[['HHL', 'ACCESS', 'WGTP']].dropna()
    
    # Calculate total sum of WGTP values in the dataset
    total_wgtp_sum = dummy_df['WGTP'].sum()

    # Define a custom aggregation function to calculate percentage
    def percentage_sum(x):
        return f"{round((x.sum() / total_wgtp_sum) * 100,2)}%"

    # Create the pivot table with percentages
    pivot_table = dummy_df.pivot_table(index='HHL', columns='ACCESS', values='WGTP', aggfunc=percentage_sum, fill_value=0, margins=True, margins_name='ALL')
    
    # Set name for row index
    pivot_table.index.name = 'HHL - Household language'
    
    # Rename index and columns using dictionaries for readability
    return pivot_table.rename(index=household_language, columns=internet_access)


# Function to perform quantile analysis of household income
def quantile_analysis_of_HINCP():
   # Create income quantiles
    hill_df['income_quantile'] = pd.qcut(hill_df['HINCP'], labels=['low', 'medium', 'high'], q=3).dropna()
    
    # Group by 'income_quantile' and aggregate for 'HINCP' and 'WGTP'
    aggregated_df = hill_df.groupby('income_quantile', observed=False).agg({
        'HINCP': ['min', 'max', 'mean'],  # Calculate min, max, and mean of 'HINCP'
        'WGTP': [('household_count', 'sum')]  # Calculate sum of 'WGTP' and label the column as 'household_count'
    })
    
    # Drop the top level of the multi-index columns
    aggregated_df.columns = (aggregated_df.columns.droplevel(0))
    
    # Set the index name to 'HINCP'
    aggregated_df.index.name = 'HINCP'
    
    # Return the aggregated DataFrame
    return aggregated_df



def main():
    
    #assignment information
    print_assignment_information(7)
    
    # Print Table 1 header - Descriptive Statistics of HINCP, grouped by HHT
    print("*** Table 1 - Descriptive Statistics of HINCP, grouped by HHT ***\n")
    
    # Call the function to generate and print descriptive statistics of household income by household type
    print(household_income_by_HHT())   
    
    # Print Table 2 header - HHL vs. ACCESS - Frequency Table
    print(f"""\n*** Table 2 - HHL vs. ACCESS - Frequency Table ***
                                                 Sum
                                                 WGTP""")
    # Call the function to generate and print the frequency table of household language vs. internet access
    print(houehold_language_vs_access())
    
    # Print Table 3 header - Quantile Analysis of HINCP - Household income (past 12 months)
    print("\n*** Table 3 - Quantile Analysis of HINCP - Household income (past 12 months) ***\n")
    
    # Call the function to generate and print quantile analysis of household income
    print(quantile_analysis_of_HINCP())
    

if __name__ == "__main__":
    main()
    # Set the maximum number of columns to display in pandas DataFrames to 500.
    pd.set_option('display.max_columns', 500)
    # Set the maximum width of the display in characters for pandas DataFrames to 1000.
    pd.set_option('display.width', 1000)

    