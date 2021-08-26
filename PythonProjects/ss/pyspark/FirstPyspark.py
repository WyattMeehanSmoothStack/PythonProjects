import collections

from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
    sc = SparkContext(conf=conf)

    lines = sc.textFile("C:/Users/meeha/OneDrive/Desktop/SmoothStack/Data/ml-100k/u.data")
    ratings = lines.map(lambda x: x.split()[2])

    # list_ratings = ratings.collect()
    # print(len(list_ratings))

    result = ratings.countByValue()
    print(result)

    sortedResults = collections.OrderedDict(sorted(result.items()))
    for key, value in sortedResults.items():
        print("%s %i " % (key, value))
