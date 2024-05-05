#Define the function to print the assignment information
def print_assignment_information(assignment_number):
    print(
f"""
DATA-5110, [1st Sem] [2024]
NAME: Manish Neupane
PROGRAMMING ASSIGNMENT #{assignment_number}
"""
        )
    
# Define the function to compute mean and variance using online algorithm
def update_mean_and_variance(positive_number):
    global previous_mean, previous_variance, number_of_element
    
    # Increment the number of elements entered
    number_of_element += 1
    
    # Calculate the new mean using the updated previous mean and the new number
    new_mean = previous_mean + ((positive_number - previous_mean) / number_of_element)
    1
     # If there is more than one element entered, compute the new variance using online algorithm
    if number_of_element > 1:
        #break the variance calculation into two half for easy calculation
        #Compute the variance contribution, adjusting based on total count of value seen.
        first_half = ((number_of_element - 2) / (number_of_element - 1)) * previous_variance
        # Compute the second half squaring the difference between the new value and the previous mean,
        #and dividing by the total number of data points.
        second_half = ((positive_number - previous_mean) ** 2) / number_of_element
        # Combine the two halves to get the new variance
        new_variance = (first_half + second_half)
    #else  only one element is entered, set the variance to 0
    else:
        new_variance = 0.0
        
    # Update the previous mean and variance variables with the new mean and variance
    previous_mean=new_mean
    previous_variance=new_variance
    
    # Print the new mean and variance with appropriate rounding to match the output exactly
    print(f'Mean is {new_mean}  variance is {round(new_variance, 11)}','\n')

# Entry point of the program
if __name__ == "__main__":
     #call print assignment information function
    print_assignment_information(assignment_number=1)
    # Initialize variables to store previous mean, previous variance, and number of elements
    previous_mean = 0
    previous_variance = 0
    number_of_element = 0
    
    # Prompt the user to enter a number and store it in the variable num
    num = int(input("Enter the number : "))
    
    # Continuously prompt the user to enter numbers until a negative number is entered
    while num >= 0:
        # Call the compute function to calculate the mean and variance for the entered number
        update_mean_and_variance(num)
        # Prompt the user to enter the next number
        num = int(input("Enter the number : "))
