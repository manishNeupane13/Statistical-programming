#declare the feature cluster dict variable to store feature as key and cluster as value for writing the feature wise output in a file
global feature_cluster_dict
#Define the function to print the assignment information
def print_assignment_information(assignment_number):
    print(
f"""
DATA-5110, [1st Sem] [2024]
NAME: Manish Neupane
PROGRAMMING ASSIGNMENT #{assignment_number}
"""
        )
#method to read initial the data from txt file
def read_initial_data(filename):
    #open and read the file
    
    with open(filename,'r') as readdata:
        
    #read the data from the file, strip newlines and split by newline characters
        features=[float(each_line) for each_line in ((readdata.read().strip('\n').split("\n")))] #convert each line to a float
        
        return (features)  #return the list of features read from the txt file
    
#helper method to calcuate the euclidean distance
def calc_distance(centroids,feature):
    #return the squared distance between each centroid and the given feature calculation
    return [((feature-each_centroid)**2) for each_centroid in list(centroids.values())]

#method to assign each features to the particular cluster
def assign_features_to_cluster(centroids,features):
    
    # Initialize a dictionary with cluster indices as keys and empty lists as values.
    features_assigned_with_clusters=dict(zip(range(number_of_cluster),[[] for i in range(number_of_cluster)]))
    
    # Iterate over features and assign each to its closest centroid's cluster.
    for index in range(len(features)):
    
         # Calculate distances from centroids to the current feature.
        distance_from_centroids=(calc_distance(centroids,features[index]))
    
        # Find the index of the centroid with minimum distance.
        mini_centroid_index=(distance_from_centroids.index(min(distance_from_centroids)))
    
        # Add the feature to the cluster corresponding to the closest centroid.
        features_assigned_with_clusters[mini_centroid_index].append(features[index])
    
        # Update the feature_cluster_dict with the assigned cluster for the current feature.
        feature_cluster_dict[features[index]]=mini_centroid_index 
    
    return (features_assigned_with_clusters) # Return the dictionary with features assigned to clusters.
    
    
def get_updated_centroid_value(features_assigned_with_clusters):
    # Calculate the mean value of all the features for each cluster and update centroids accordingly.
    # x is the cluster and y is the features 
    # first part of zip gets the cluster and store it as key 
    # second part of zip store the centroid 
    update_centroids=dict(zip((x for x in features_assigned_with_clusters.keys()),(sum(y)/len(y) for y in features_assigned_with_clusters.values())))
    
    return update_centroids # Return the updated centroids


def display_each_iteration(features_assigned_with_clusters):
    # Display each cluster along with the features assigned to it.
    for cluster,features in features_assigned_with_clusters.items():
    
        print(cluster,features) #print cluster and the features associated
                    
def write_output_into_file(filename):
    # Write each feature along with its assigned cluster into the output file.
    with open(filename, 'w') as file:
       
        file.write("Output File Contents\n") #write header of the file
       
        for feature, cluster in feature_cluster_dict.items(): #iterate over the feature_cluster dict 
            output_format=f'Point {feature} in Cluster {cluster}' #store output format in a variable 
            file.write(f'{output_format}\n')  #write the output in a file
            print(f'{output_format}') # Print the output for display purposes.

def Kmeans_clustering(filename,number_of_cluster):
    # Read the features from the input file.
    features =read_initial_data(filename) 
    # Initialize centroids with the first 'number_of_cluster' features.
    centroids=dict(zip(range(number_of_cluster),features[0:number_of_cluster])) 
    
    iteration = 1 # Initialize iteration counter.
    while True:
        # Assign features to clusters based on current centroids.
        features_assigned_with_clusters= assign_features_to_cluster(centroids, features)
        
        # Calculate updated centroids based on the assigned clusters.
        new_centroids = get_updated_centroid_value(features_assigned_with_clusters)
        
        print("\nIteration", iteration)
        
        display_each_iteration(features_assigned_with_clusters) # Display current clusters.
        
        if new_centroids == centroids:  # Check for convergence.
            print() # Print a newline for readability.
            break #break the loop if new centroids  match with previous centroids
        
        centroids = new_centroids # Update centroids .
        iteration += 1 # Increment iteration counter.
    
    write_output_into_file("prog2-output-data.txt") # Write the output to a file.
    
                  

if __name__=="__main__":
    # print the assignment information 
    print_assignment_information(assignment_number=2)
    
    # variable declaration to store featurs and their assigned cluster
    feature_cluster_dict={}
    
    # prompt the user to input the number of clusters
    number_of_cluster=int(input("Enter the number of clusters : ")) 
    
    # Kmeans_clustering function and pass the initial data file and the number of cluster
    Kmeans_clustering("prog2-input-data.txt",number_of_cluster)
   
    
    
            