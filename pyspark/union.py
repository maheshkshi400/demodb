# Python program to illustrate the
# working of union() function
import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('GeeksforGeeks.com').getOrCreate()

# Creating a dataframe
data_frame1 = spark.createDataFrame(
	[("Bhuwanesh", 82.98), ("Harshit", 80.31)],
	["Student Name", "Overall Percentage"]
)

# Creating another dataframe
data_frame2 = spark.createDataFrame(
	[("Naveen", 91.123), ("Piyush", 90.51)],
	["Student Name", "Overall Percentage"]
)

# union()
answer = data_frame1.union(data_frame2)

# Print the result of the union()
answer.show()
