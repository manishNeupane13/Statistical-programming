
import pandas as pd
import re

# File path to the CSV file
file_path = 'cps.csv'


#method to print assignment information
def print_assignment_information(assignment_number):
    print(
f"""
DATA 5100 - [1st Semester] [2024]
NAME: Manish Neupane
PROGRAMMING ASSIGNMENT {assignment_number}



"""
        )

# Function to extract starting hour from 'School_Hours' column
def get_starting_hour(data_series):
    get_time = (re.findall("[0-9]+", str(data_series)))
    if len(get_time) != 0:
        return int(get_time[0])

# Function to get the lowest grade offered from 'Grades_Offered_All' column
def get_lowest_grade_offered(data_series):
    return data_series.split(',')[0]

# Function to get the highest grade offered from 'Grades_Offered_All' column
def get_highest_grade_offered(data_series):
    splited_data = data_series.split(',')
    highest_grade_index = len(splited_data) - 1
    return splited_data[highest_grade_index]

# Function to preprocess the data and create new columns
def preprocess_data(cps_df):
    
    # List of columns to be selected
    columns = ['School_ID', 'Short_Name', 'Is_High_School', 'Zip', 'Student_Count_Total', 'College_Enrollment_Rate_School','Lowest_Grade','Highest_Grade','School_Start_Hour']
    
    # Handling missing values in 'College_Enrollment_Rate_School' column by filling with the mean
    cps_df['College_Enrollment_Rate_School'].fillna(cps_df['College_Enrollment_Rate_School'].mean(), inplace=True)
    
    # Applying the functions to create new columns
    cps_df['School_Start_Hour'] = cps_df['School_Hours'].apply(get_starting_hour)
    cps_df['Lowest_Grade'] = cps_df['Grades_Offered_All'].apply(get_lowest_grade_offered)
    cps_df['Highest_Grade'] = cps_df['Grades_Offered_All'].apply(get_highest_grade_offered)
    return cps_df[columns] #return only the selected columns

# Function to calculate mean and standard deviation of college enrollment rate for high schools
def calculate_college_enrollment(cps_df):
    highSchool_collegeEnroll_mean = cps_df[cps_df['Is_High_School'] == True]['College_Enrollment_Rate_School'].mean()
    highSchool_collegeEnroll_std = cps_df[cps_df['Is_High_School'] == True]['College_Enrollment_Rate_School'].std()
    return highSchool_collegeEnroll_mean, highSchool_collegeEnroll_std

# Function to calculate mean and standard deviation of student count for non-high schools
def calculate_student_count(cps_df):
    NonHighSchool_Student_count = cps_df[cps_df['Is_High_School'] == False]['Student_Count_Total'].mean()
    NonHighSchool_Student_std = cps_df[cps_df['Is_High_School'] == False]['Student_Count_Total'].std()
    return NonHighSchool_Student_count, NonHighSchool_Student_std

# Function to count distribution of starting hours
def count_starting_hours(cps_df):
    start_hour_distribution = cps_df['School_Start_Hour'].value_counts()
    return start_hour_distribution

# Function to count number of schools outside the Loop
def count_schools_outside_loop(cps_df):
    loop_zip_code = [60601, 60602, 60603, 60604, 60605, 60606, 60607, 60616]
    schools_outside_loop = cps_df[~cps_df["Zip"].isin(loop_zip_code)].shape[0]
    return schools_outside_loop

# Main function
def main():
    print_assignment_information(5)
    # Reading the CSV file into a DataFrame
    cps_df = pd.read_csv(file_path)
   
    # Preprocessing the data
    new_cps_df = preprocess_data(cps_df)

    # Displaying the first 10 rows of the DataFrame
    print(new_cps_df.head(10))
    
    # Calculating college enrollment rate for high schools
    highSchool_collegeEnroll_mean, highSchool_collegeEnroll_std = calculate_college_enrollment(new_cps_df)
    print(f'\nCollege Enrollment Rate for High Schools = {round(highSchool_collegeEnroll_mean, 2)} (sd={round(highSchool_collegeEnroll_std, 2)})')
    
    # Calculating student count for non-high schools
    NonHighSchool_Student_count, NonHighSchool_Student_std = calculate_student_count(new_cps_df)
    print(f'\nTotal Student Count for non-High Schools = {round(NonHighSchool_Student_count, 2)} (sd={round(NonHighSchool_Student_std, 2)})')
    
    # Counting distribution of starting hours
    start_hour_distribution = count_starting_hours(new_cps_df)
    print('\nDistribution of Starting Hours:')
    for index, values in start_hour_distribution.items():
        print(f'{int(index)}am', values)
    
    # Counting number of schools outside the Loop
    schools_outside_loop = count_schools_outside_loop(new_cps_df)
    print(f'\nNumber of School outside Loop: {schools_outside_loop}')

if __name__ == "__main__":
    main()


