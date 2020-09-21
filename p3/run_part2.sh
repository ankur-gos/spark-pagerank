hdfs dfs -rm -r /output/part2_output
/users/yunjia/spark-2.4.7-bin-hadoop2.7/bin/spark-submit part2_spark_sort.py local hdfs://10.10.1.1:9000/input/export.csv hdfs://10.10.1.1:9000/output/part2_output