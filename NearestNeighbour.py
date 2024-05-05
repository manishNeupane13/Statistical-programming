import numpy as np
# define the function to print the assignment information
def print_assignment_information(assignment_number):
    print(
f"""
DATA-5110, [1st Sem] [2024]
NAME: Manish Neupane
PROGRAMMING ASSIGNMENT #{assignment_number}
"""
        )
# function to calculate the euclidean distance between two points
def euclidean_distance(x1,x2):
    return np.sqrt(np.sum((x1-x2)**2,axis=1))

# function to read data from the csv file 
def read_data(filename):
    X=(np.loadtxt(filename,delimiter=",",usecols=range(4)))
    y=(np.loadtxt(filename,dtype='<U',delimiter=",",usecols=4))
    return X,y

# class implementing the Nearest Neighbours algorithm
class NearestNeighbour:
    
    def __init__(self,K=1): #default value is set to 1
        #initialize the number of neighbors to consider 
        self.k=K
        
    # method to fit the model to the training data
    def fit(self,X_train,y_train):
        self.x_train=X_train
        self.y_train=y_train
        
    # method to predicted the labels for the test data
    def predict(self,x_test):
        # calculate the distance between the test data and training data
        distance=euclidean_distance(x_test, self.x_train)
        # sort the distance in ascending order 
        sorted_close_distance_indices=(np.argsort(distance,kind='mergesort'))
        # get the indices of the first nearest neighbors
        K_neigbour_indices=sorted_close_distance_indices[:self.k]
        # return the labels of the first nearest neighbours
        return y_train[K_neigbour_indices]
    
    # method to display the output: index, true label, predicted label   
    def display_output(self,y_predicted,y_test):
        
        # Generate indices from 1 to the length of the arrays
        indices = np.arange(0, len(y_predicted))
        
        # print the index, true label and predicted label for each index
        print(f'#, True, Predicted')
        
        # Zip together the indices, true labels (y_test), and predicted labels (y_predicted) 
        # to iterate over them simultaneously and format the output string for each item
        print(*[f"{index+1}, {test_val}, {predicted_val}" for index,test_val,predicted_val in zip(indices,y_test,y_predicted)], sep='\n')
    
    # method to calculate and return the accuray score
    #takes in y_predicted, y_test as parameters
    def accuracy_score(self,y_predicted,y_test):
        # check if the predicted lables match the true labels
        result=y_predicted==y_test 
        #calculate the accuray as the proportion of correct predictions
        return round((np.mean(result))*100,2)
        
#main function to run the program
if __name__=="__main__":
    # read training data
    X_train,y_train=read_data("iris-training-data.csv")
    # readtesting data
    X_test,y_test=read_data("iris-testing-data.csv")
    # create an instance of NearestNeighbour class
    Model=NearestNeighbour()
    #fit the model to the training data
    Model.fit(X_train, y_train)
    #predict the labels for the test data
    #Apply the predict method along the first axis (rows) of the test data array (X_test)
    y_predicted=(np.apply_along_axis(Model.predict, axis=1, arr=X_test)).reshape(-1) 
    # run the assignment information method
    print_assignment_information(3)
    # display the output
    Model.display_output(y_predicted,y_test)
    #calculate and print the accuray score
    print(f'{Model.accuracy_score(y_test,y_predicted)}%')
    

