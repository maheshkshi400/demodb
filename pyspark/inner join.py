# Python program to illustrate the
# working of union() function
import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('maheshdemo.com').getOrCreate()

# Creating a dataframe
data_frame1 = spark.createDataFrame(
	[(1,"Bhuwanesh", 82.98), (2,"Naveen", 91.123)],
	["id","Student Name", "Overall Percentage"]
)

# Creating another dataframe
data_frame2 = spark.createDataFrame(
	[(2,"Naveen", 91.123), (1,"Piyush", 90.51)],
	["id","Student Name", "Overall Percentage"]
)

# inner join()
answer1 = data_frame1.join(data_frame2,data_frame1.id==data_frame2.id,'inner')

# Print the result of the union()
answer1.show()

# inner join()
answer2 = data_frame1.join(data_frame2,data_frame1.id==data_frame2.id,'left')

# Print the result of the union()
answer2.show()