# Import SparkSession
from pyspark.sql import SparkSession



# Create SparkSession 
spark = SparkSession.builder \
      .master("local[1]") \
      .appName("SparkByExamples.com") \
      .getOrCreate() 


data = [(1,'mahesh','male',20,5000,'IT',50,9870678902),\
        (2,'shruthi','female',30,6000,'HR',20,8975679046),\
        (3,'ganesh','male',25,7000,'FINANCE',30,9096115677),\
        (4,'pooja','female',34,8000,'PAYROLL',40,9090879076),\
        (5,'kamini','female',31,6000,'IT',50,9090912345),\
        (6,'shivaji','male',20,8000,'IT',50,9081234579),\
        (7,'shruthi','female',30,6000,'HR',20,9087957856),\
        (8,'suresh','male',25,10000,'FINANCE',30,9175468990),\
        (9,'shivani','female',34,11000,'PAYROLL',40,9175468990),\
        (10,'prachi','female',30,6000,'IT',50,9177899076)]

schema1 = ['id','name','gender','age','salary','dept','deptno','contactno']


df2 = spark.createDataFrame(data=data,schema=schema1)
df2.show()



