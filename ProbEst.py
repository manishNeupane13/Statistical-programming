
import pandas as pd


def print_assignment_information(assignment_number):
    """
    Print assignment information including course, semester, student name, and assignment number.

    Parameters:
    assignment_number (int): The number of the programming assignment.
    """
    print(
f"""
Data-51100, [1st Semester] [2024]
NAME: Manish Neupane
PROGRAMMING ASSIGNMENT #{assignment_number}
""")

def get_estimated_probability_of_two_columns(data_frame, X_feature_column, F_feature_column):
    """
    Calculate the estimated probability of X_feature_column given F_feature_column and print the results.

    Parameters:
    data_frame (DataFrame): The DataFrame containing the data.
    X_feature_column (str): The name of the column for which probability is estimated.
    F_feature_column (str): The name of the column on which the probability estimation is based.
    """
    # Loop through unique values of F_feature_column
    for F_each_distinct_val in data_frame[F_feature_column].unique():
        # Calculate the count of occurrences of F_feature_column value
        prob_of_F_count = data_frame.query(f'{F_feature_column} == "{F_each_distinct_val}"').shape[0]

        # Loop through unique values of X_feature_column
        for X_each_distinct_val in data_frame[X_feature_column].unique():
            # Calculate the count of occurrences of both X_feature_column and F_feature_column values
            prob_of_X_and_F_count = data_frame.query(f'{X_feature_column} == "{X_each_distinct_val}" and {F_feature_column} == "{F_each_distinct_val}"').shape[0]
            
            # Calculate and print the probability of X_feature_column given F_feature_column
            estimated_probability = round((prob_of_X_and_F_count / prob_of_F_count) * 100,2)
            
            print(f'Prob({X_feature_column}={X_each_distinct_val}|{F_feature_column}={F_each_distinct_val})= {estimated_probability}%')
        
    print()


def get_proability_of_single_colum(data_frame,column_name): 
    """
    Calculate the probability of each distinct value in a single column and print the results.

    Parameters:
    data_frame (DataFrame): The DataFrame containing the data.
    column_name (str): The name of the column for which probability is calculated.
    """
    # Calculate total number of data points in the column
    total_data_count=(data_frame[column_name].count())
    # Loop through unique values of the column
    for distinct_val in data_frame[column_name].unique():
        # Calculate the count of occurrences of each distinct value
        each_distinct_val_count=(data_frame[[column_name]].query(f'{column_name}=="{distinct_val}"').shape[0])
        # Calculate the percentage of occurrences of each distinct value
        percentage_value=(round(((each_distinct_val_count/total_data_count)*100),2))
        print(f'Prob({column_name}={distinct_val}) = {percentage_value}%')
        

if __name__=="__main__":
    # Read the data from the 'cars.csv' file into a DataFrame
    path='cars.csv'
    car_df=pd.read_csv(path)
    
    # Print assignment information for assignment number 4
    print_assignment_information(4)
    
    # Calculate and print estimated probabilities of two columns ('aspiration' and 'make')
    get_estimated_probability_of_two_columns(car_df, 'aspiration', 'make')
    
    # Calculate and print probabilities of single column ('make')
    get_proability_of_single_colum(car_df,'make')
