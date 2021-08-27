from pyspark.sql import Row
from pyspark.sql import SparkSession


def mapper(line):
    fields = line.split(",")
    return  Row(ID=int(fields[0]), cost=float(fields[2]))


if __name__ == '__main__':
    spark = SparkSession.builder.appName("SparkSQL").getOrCreate()
    lines = spark.sparkContext.textFile("C:/Users/meeha/OneDrive/Desktop/SmoothStack/Data/customer-orders.csv")
    transactions = lines.map(mapper)
    schema_cus = spark.createDataFrame(transactions).cache()
    schema_cus.createOrReplaceTempView("transactions")
    total_costs = spark.sql("Select ID, sum(cost) From transactions Group By ID Order By ID")
    for cus_id, cost in total_costs.collect():
        print("CustomerId: {} Total Bill: {:0.2f}".format(cus_id, cost))
