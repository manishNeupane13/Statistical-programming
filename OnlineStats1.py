#method to print the assignment information
def print_assignment_information(assignment_number):
    print(
f"""
DATA-5110, [1st Sem] [2024]
NAME: Manish Neupane
PROGRAMMING ASSIGNMENT #{assignment_number}
"""
        )
    
class MeanCalculation:
    #initialize the required variables for the calculation
    def __init__(self):
        self.number_of_value=0
        self.mean_value=0
        self.variance_value=0
    #method to implement the algorithim to get the calculaiton
    def update_mean_and_variance(self,positiveNumber):
        #increase the number of value 
        self.number_of_value+=1
        #store the previous mean before any update
        previous_mean=self.mean_value
        #update the value of mean 
        self.mean_value=previous_mean+((positiveNumber-self.mean_value)/self.number_of_value)
        #update and calculate the variance only if total number of values are more than 1
        if self.number_of_value>1:
            #breaking the algorithm in two half
            #First, calculating the variance contribution, adjusting based on total count of value seen.
            first_half=(((self.number_of_value-2)/(self.number_of_value-1))*(self.variance_value))
            # #Second, squaring the difference between the new value and the previous mean,
            # #and dividing by the total number of data points.
            second_half=(((positiveNumber-previous_mean)**2)/self.number_of_value)
            # #update the variance value as the sum of first_half and second_half.
            self.variance_value=first_half+second_half
            
            # (((self.number_of_value-2)/(self.number_of_value-1))*(self.variance_value))+(((positiveNumber-previous_mean)**2)/self.number_of_value)
           
           
            
            # first_half+second_half
        #display the value of mean and the variance
        print(f'Mean is {self.mean_value}  variance is {round(self.variance_value,11)}','\n')
    
        
if __name__=="__main__":
    #print assignment information
    print_assignment_information(assignment_number=1)
    #create object for Mean calculation
    calc_obj=MeanCalculation()
    #get number from the user
    positiveNumber=int(input("Enter the number: "))
    #run the loop if the number is non-negative only
    while positiveNumber>=0: 
        #calling calculation method that implements the mean and variance algorithm
        calc_obj.update_mean_and_variance(positiveNumber)
        #again ask the user for getting other values 
        positiveNumber=int(input("Enter the number: "))