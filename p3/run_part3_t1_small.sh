hdfs dfs -rm -r /out/part3_t1_small_output
start=`date +%s`
/users/yunjia/spark-2.4.7-bin-hadoop2.7/bin/spark-submit part3_t1_spark_pagerank.py spark://172.16.86.1:7077 hdfs://10.10.1.1:9000/input/web-BerkStan.txt hdfs://10.10.1.1:9000/output2/part3_t1_small_output
# python3 part3_spark_pagerank.py local ./data/part3/web-BerkStan.txt hdfs://10.10.1.1:9000/output/part3_t1_output
end=`date +%s`

echo runtime=$((end-start)) >> part3_t1_small.log