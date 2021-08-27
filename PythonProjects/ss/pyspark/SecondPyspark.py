from pyspark import SparkConf, SparkContext
from pyspark import sql


def parse_line(line):
    fields = line.split(",")
    customer = int(fields[0])
    order_total: float = float(fields[2])
    return customer, order_total


if __name__ == '__main__':
    conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
    sc = SparkContext(conf=conf)
    sqlContext = sql.SQLContext(sc)

    lines = sc.textFile("C:/Users/meeha/OneDrive/Desktop/SmoothStack/Data/customer-orders.csv")
    parsed_lines = lines.map(parse_line)

    data = parsed_lines.collect()
    order_rdd = sc.parallelize(data)
    order_rdd = order_rdd.reduceByKey(lambda x, y: x + y).sortByKey()

    data = order_rdd.collect()
    for row in data:
        print("CustomerId: {} Cost: {:0.2f}".format(row[0], row[1]))
