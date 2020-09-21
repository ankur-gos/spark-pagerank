import sys
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from operator import add


def large_file_filter_fn(line):
    """
    Filter out the lines that we don't need
    """
    line = line.lower()
    tokens = line.split("\t")

    if len(tokens) <= 1:
        return False
    elif len(tokens) > 2:
        return False
    elif ":" in tokens[0] and "category:" not in tokens[0].lower():
        return False
    elif ":" in tokens[1] and "category:" not in tokens[1].lower():
        return False
    else:
        return True


def small_file_filter_fn(line):
    if '#' in line:
        return False
    else:
        return True


def map_pairs_fn(line):
    nodes = line.split('\t')
    return (nodes[0], nodes[1])


def println(line):
    print(line)


def flatMap_fn(line):
    num = len(line[0])
    scores = []
    for n in line[0]:
        scores.append((n, line[1] / len(line[0])))
    return scores


# def add_ranks():
#     return add


def calculate_page_rank(lines, m_filter_fn):
    """
    Filter out the data that is not useful
    map lines into pairs of nodes
    distinct() is to filter out the duplicate edges
    """
    neighbors = lines.filter(m_filter_fn).map(
        map_pairs_fn).distinct().groupByKey().cache()

    """
    Set default pagerank to 1
    """
    rank = neighbors.mapValues(lambda rank: 1)

    for i in range(10):
        """ 
        "update" is the update value of pagerank
        """
        update = neighbors.join(rank).values().flatMap(flatMap_fn)
        rank = update.reduceByKey(
            add).mapValues(lambda rank: 0.15 + 0.85 * rank)
    return rank


if __name__ == "__main__":
    argv = sys.argv
    master = argv[1]
    file_path = argv[2]
    save_path = argv[3]

    if 'xml' in file_path or 'wiki' in file_path:
        m_filter_fn = large_file_filter_fn
        partition_size = 500
        App_name = 'Part3-t3-large-partition-%d' % partition_size
    else:
        m_filter_fn = small_file_filter_fn
        partition_size = 5
        App_name = 'Part3-t3-small-partition-%d' % partition_size

    conf = SparkConf().setAppName(
        App_name).setMaster(master).set("spark.local.dir", "/mnt/data/tmp/").set("spark.eventLog.enabled", "true").set("spark.driver.memory", "25g").set("spark.executor.memory", "25g").set("spark.executor.cores", "5").set("spark.tmp.dir", "/mnt/data/tmp/").set("spark.eventLog.dir", "file:///users/yunjia/spark_log/")
    sc = SparkContext(conf=conf)

    lines = sc.textFile(file_path).repartition(partition_size)

    rank = calculate_page_rank(lines, m_filter_fn)

    rank.saveAsTextFile(save_path)
