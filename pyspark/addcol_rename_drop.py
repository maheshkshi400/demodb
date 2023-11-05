import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('https://github.com/maheshkshi400/demo1408').getOrCreate()



data1 = [(1,'mahesh','male',20,5000,'IT',50),\
        (2,'shruthi','female',30,6000,'HR',20),\
        (3,'ganesh','male',25,7000,'FINANCE',30),\
        (4,'pooja','female',34,8000,'PAYROLL',40),\
        (5,'kamini','female',31,6000,'IT',50),\
        (6,'shivaji','male',20,8000,'IT',50),\
        (7,'shruthi','female',30,6000,'HR',20),\
        (8,'suresh','male',25,10000,'FINANCE',30),\
        (9,'shivani','female',34,11000,'PAYROLL',40),\
        (10,'prachi','female',30,6000,'IT',50)]
schema1 = ['id','name','gender','age','salary','dept','deptno']

df1 = spark.createDataFrame(data1,schema1)
df1.show()

# Add new column 
# Add new column in the table
from pyspark.sql.functions import lit,col
df2 =df1.withColumn("location",lit("INDIA"))
df2.show()