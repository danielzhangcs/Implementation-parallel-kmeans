import sys
from pyspark import SparkConf, SparkContext
import math
import  numpy as np
import timeit
import pandas as pd

"""This method is responsible for selecting k initial points and return it as a list of points"""
def select_initial_centroid(lines,k):
    lines = lines.map(lambda l: [int(x) for x in l.split(",")])
    centroid_list=lines.takeSample(False, k)
    return centroid_list



"""This is the map method which will process each line to find the closest centroid and return a key key value pair, key is the 
index of centroid and value is the line"""
def map(centroid_list, lines):
    processed_lines = lines.map(lambda l: (find_the_closest_centroid(l, centroid_list), l))
    return processed_lines


"""This method will calculate the distance between a point and all centroid and return the index of the one
with smallest distance"""
def find_the_closest_centroid(l, centroid_list):
    instance = [int(x) for x in l.split(",")]
    closest_index=-1
    smallest_distance = float('inf')
    for i in range(0, len(centroid_list)):
        distance = sum([(a - b) ** 2 for a, b in zip(instance, centroid_list[i])])
        if distance < smallest_distance:
            smallest_distance = distance
            closest_index = i
    return closest_index


"""This is the combiner method which will firstly create a initial status which convert the instance into array
and create another 1 after it to log the total number of pints assigned to same index. Then keep add all the points together 
and return the list and number of list as value"""
def combineByKey(lines_with_index):
    lines=lines_with_index.map(lambda l: (l[0], [int(x) for x in l[1].split(",")]))
    sumCount = lines.combineByKey(lambda value:(np.array(value), 1),
                                 lambda x, value: (x[0]+ np.array(value), x[1] + 1),
                                 lambda x, y: (list(x[0] + y[0]), x[1] + y[1]))
    return sumCount


"""This method will update centroid list based on the result of combiner and collect the result"""
def update_centroids(sumCount):
     new_centroids=sumCount.map(lambda t: [i/t[1][1] for i in t[1][0]]).collect()
     return new_centroids


"""This method will calculate the distance between 2 points"""
def calculate_distance(list1, list2):
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(list1, list2)]))

"""This methos will call all the methods defined above to conduct parallel k-means on a data
and print the number of iterations and time it spend to converge"""
def P_Kmeans(lines,k):
    centroid_list = select_initial_centroid(lines, k)
    iteration = 0
    change = float('inf')
    start = timeit.default_timer()
    while change > 500:
        change = 0
        lines_with_index = map(centroid_list, lines)
        sumCount = combineByKey(lines_with_index)
        new_centroid = update_centroids(sumCount)
        for i in range(0, len(centroid_list)):
            change += calculate_distance(centroid_list[i], new_centroid[i])
        centroid_list = new_centroid
        iteration += 1
        print(iteration)
        print(change)

    stop = timeit.default_timer()
    print("Time : ", stop - start)


"""This method will randomly select sample data with different size and store them in the path user specified"""
def process_data(path, data_name):

    df = pd.read_csv(path+data_name, sep=',',header=None)
    df1=df.sample(frac=0.125)
    df1.to_csv(path+"data1.csv", sep=',', index=False)
    df.sample(frac=0.25).to_csv(path+"data2.csv", sep=',', index=False)
    df.sample(frac=0.5).to_csv(path+"data3.csv", sep=',', index=False)
    df.to_csv(path+"data4.csv", sep=',', index=False)

if __name__ =="__main__":
    k=int(sys.argv[3])
    path=sys.argv[1]+"/"
    data_name = sys.argv[2]

    conf = SparkConf()
    sc = SparkContext(conf=conf)

    process_data(path,data_name)


    # K-means for 1/8 data
    lines1 = sc.textFile(path+"data1.csv")
    P_Kmeans(lines1,k)

    # # K-means for 1/4 data
    # lines2 = sc.textFile(path+"data2.csv")
    # P_Kmeans(lines2,k)
    #
    #
    # # K-means for 1/2 data
    # lines3 = sc.textFile(path+"data3.csv")
    # P_Kmeans(lines3,k)
    #
    # # K-means for whole data
    # lines4 = sc.textFile(path+"data4.csv")
    # P_Kmeans(lines4,k)
    #




