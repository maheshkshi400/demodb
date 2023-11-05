import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('https://github.com/maheshkshi400/demo1408').getOrCreate()



data1 = [(1,'mahesh','male',20,5000,'IT',50),
         (2,'shruthi','female',30,6000,'HR',20),
         (3,'ganesh','male',25,7000,'FINANCE',30),
         (4,'pooja','female',34,8000,'PAYROLL',None),
         (5,'kamini','female',31,6000,None,40)]
schema1 = ['id','name','gender','age','salary','dept','deptno']

df1 = spark.createDataFrame(data1,schema1)
df1.show()


# Method 1
(df1.filter(df1.salary==5000)).show()

# method2 (using &,|)
df3= df1.filter((df1.salary==5000) & (df1.deptno==50)).show()
df4= df1.filter((df1.salary==8000) | (df1.age==34)).show()


# method 3 (Startswith,endswith,contains)
df5= df1.filter((df1.name.startswith('p'))).show()
df6= df1.filter((df1.name.endswith('i'))).show()
df7= df1.filter((df1.name.contains('o'))).show()

# Method 4  (isNull,isNotNull)
df8= df1.filter((df1.dept.isNull())).show()
df9= df1.filter((df1.deptno.isNotNull())).show()

# Method 5 (isin)
df8= df1.filter((df1.salary.isin(5000,7000))).show()

# Method 6
df9= df1.filter((df1.name.like('kamini'))).show()



