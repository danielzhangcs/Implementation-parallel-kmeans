{\rtf1\ansi\ansicpg936\cocoartf1561\cocoasubrtf600
{\fonttbl\f0\froman\fcharset0 TimesNewRomanPSMT;\f1\fswiss\fcharset0 Helvetica;\f2\froman\fcharset0 Times-Roman;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\margl1440\margr1440\vieww25100\viewh12980\viewkind0
\deftab420
\pard\pardeftab420\ri720\sl240\qj\partightenfactor0

\f0\fs21 \cf0 \
\pard\pardeftab420\ri720\sl240\partightenfactor0

\f1\b\fs24 \cf0 Title
\b0 : \
\pard\pardeftab720\sl440\sa240\partightenfactor0

\f2\b\fs26 \cf2 \expnd0\expndtw0\kerning0
Spark Program to replicate the Parallel K-means experiment
\f1\b0\fs22 \cf0 \kerning1\expnd0\expndtw0 \uc0\u8232 
\b \
\pard\pardeftab420\ri720\sl240\partightenfactor0

\fs24 \cf0 Author
\b0 : \
\pard\pardeftab420\ri720\sl240\partightenfactor0

\fs26 \cf0 Daniel Zhang
\fs22 	\uc0\u8232 
\b \
\pard\pardeftab420\ri720\sl240\partightenfactor0

\fs24 \cf0 Date
\b0 : \
\pard\pardeftab420\ri720\sl240\partightenfactor0

\fs26 \cf0 March 2nd, 2019
\fs22 \uc0\u8232 
\b \
\pard\pardeftab420\ri720\sl240\partightenfactor0

\fs24 \cf0 Description
\b0 : \
\
\pard\pardeftab420\ri720\sl240\partightenfactor0

\fs26 \cf0 This project will implement the parallel k-means algorithm and do experiment to run it on different number of worker nodes to see the increase of efficiency
\fs22 \
\
\pard\pardeftab720\sl360\sa240\partightenfactor0

\f2\b\fs28 \cf2 \expnd0\expndtw0\kerning0
Dependencies:
\b0\fs32 \uc0\u8232 
\fs29\fsmilli14667 This program was run on python3.7. And here are some packages used to run the profile: \

\fs24 Pyspark: https://spark.apache.org/docs/2.1.3/api/python/pyspark.html \
numpy: http://www.numpy.org \
Pandas: https://pandas.pydata.org \
Some other packages such as math, sys, timeit etc. can be directly imported, no need to do \'93Pip install\'94 \
\pard\pardeftab420\ri720\sl240\partightenfactor0

\f1\fs22 \cf0 \kerning1\expnd0\expndtw0 \uc0\u8232 \
\pard\pardeftab420\ri720\sl240\partightenfactor0

\b\fs24 \cf0 Build Instructions
\b0 : \
\
\pard\pardeftab420\ri720\qj\partightenfactor0

\fs21 \cf0 Firstly, I designed the map function which take the k-centroids list and the RDD read from file as input. Then another function will be called to calculate distance between every centroid in the centroid list and the instance, then the index of the centroid with closest distance will be selected and returned as the key of the instance.\
\
Then a combiner function is designed to combine the RDD with same key (same centroid index). Specifically, the combiner will create a list for each centroid index and keep summing each dimension into the list for all the points assigned to the centroid. Additionally, the combiner function will put another value after the RDD instance to log the number of points assigned to each centroid.\
\
Then the reduce method will update each centroid in the centroid list by firstly summing up all the value together for each key, then divide each dimension by the number of points which is the second element in the value of each RDD.\
\
Then this process will be put into a while loop until the converge or the change between the iteration and last iteration reach to level which is acceptable. The objective of this experiment is to see how much efficiency the parallel k-means bring. So firstly, I created google Cloud clusters with 1, 2, 3, 4 worker nodes separately and split the data into 1/8, 1/4, 1/2 and whole data set. Then run the Parallel k-means for datasets in different size and compare the time used for running different datasets in different number of nodes to check the speedup, sizeup and scaleup.\
\
\pard\pardeftab720\sl360\sa240\partightenfactor0

\f2\b\fs32 \cf2 \expnd0\expndtw0\kerning0
Modules:\
select_initial_centroid(): 
\f1\b0\fs21 \cf0 \kerning1\expnd0\expndtw0 This method is responsible for selecting k initial points and return it as a list of points\

\b\fs24 map(): 
\b0\fs21 This is the map method which will process each line to find the closest centroid and return a key key value pair, key is the  index of centroid and value is the line\

\b find_the_closest_centroid(): 
\b0 This method will calculate the distance between a point and all centroid and return the index of the one with smallest distance
\f0 \

\b\fs24 combineByKey():
\b0\fs21  
\f1 This is the combiner method which will firstly create a initial status which convert the instance into array and create another 1 after it to log the total number of pints assigned to same index. Then keep add all the points together and return the list and number of list as value
\f0 \

\b\fs24 update_centroid(): 
\f1\b0\fs21 This method will update centroid list based on the result of combiner and collect the result\

\f0\b\fs24 calculate_distance(): 
\f1\b0\fs21 This method will calculate the distance between 2 points\

\f0\b\fs24 P_Kmeans(): 
\f1\b0\fs21 This methos will call all the methods defined above to conduct parallel k-means on a data and print the number of iterations and time it spend to converge\

\b Data_Process(): 
\b0 this method will process the inout data into sub data in different size for experiment use
\fs22 \
\pard\pardeftab420\ri720\sl240\partightenfactor0
\cf0 \uc0\u8232 
\b\fs24 Run Instructions
\b0 : \
\

\fs26 To Run this program, there are some parameters, the first one is the path of the csv profile you want to read and conduct k-means. next one is the name of the csv file. the third one is k- number of clusters the user want \
\
\
\pard\pardeftab420\ri720\sl240\partightenfactor0

\f0\fs24 \cf0 \
\pard\pardeftab420\ri720\sl240\partightenfactor0

\f1\fs22 \cf0 \uc0\u8232 }