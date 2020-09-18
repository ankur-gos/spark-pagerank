import sys
from pyspark.sql import SparkSession


def sort_df(df):
    return df.sort("cca2", "timestamp")


def load_df(session, csv_path):
    df = ss.read.option("inferSchema", "true").csv(csv_path).toDF("battery_level", "c02_level", "cca2", "cca3", "cn",
                                                                  "device_id", "device_name", "humidity", "ip", "latitude", "lcd", "longitude", "scale", "temp", "timestamp")
    return df


def save_df(df, save_path):
    df.coalesce(1).write.format("csv").save(save_path)


if __name__ == "__main__":
    argv = sys.argv
    master = argv[1]
    csv_path = argv[2]
    save_path = argv[3]

    ss = SparkSession.builder.appName("Sort").config(
        "Spark.sql.sources.default", "json").master(master).getOrCreate()
    df = load_df(ss, csv_path)
    save_df(sort_df(df), save_path)
