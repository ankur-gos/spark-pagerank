hdfs dfs -rm -r /output
echo Run small with partition number 5
start=`date +%s`
/users/yunjia/spark-2.4.7-bin-hadoop2.7/bin/spark-submit part3_t2_spark_pagerank.py spark://172.16.86.1:7077 hdfs://10.10.1.1:9000/input/web-BerkStan.txt hdfs://10.10.1.1:9000/output/ 5 2>  part3_t2_small.log
# python3 part3_spark_pagerank.py local ./data/part3/web-BerkStan.txt hdfs://10.10.1.1:9000/output/part3_t1_output
end=`date +%s`
echo runtime=$((end-start)) >> part3_t2_small.log

hdfs dfs -rm -r /output
echo Run small with partition number 10
start=`date +%s`
/users/yunjia/spark-2.4.7-bin-hadoop2.7/bin/spark-submit part3_t2_spark_pagerank.py spark://172.16.86.1:7077 hdfs://10.10.1.1:9000/input/web-BerkStan.txt hdfs://10.10.1.1:9000/output/ 10 2>  part3_t2_small.log
# python3 part3_spark_pagerank.py local ./data/part3/web-BerkStan.txt hdfs://10.10.1.1:9000/output/part3_t1_output
end=`date +%s`
echo runtime=$((end-start)) >> part3_t2_small.log

hdfs dfs -rm -r /output
echo Run small with partition number 20
start=`date +%s`
/users/yunjia/spark-2.4.7-bin-hadoop2.7/bin/spark-submit part3_t2_spark_pagerank.py spark://172.16.86.1:7077 hdfs://10.10.1.1:9000/input/web-BerkStan.txt hdfs://10.10.1.1:9000/output/ 20 2>  part3_t2_small.log
# python3 part3_spark_pagerank.py local ./data/part3/web-BerkStan.txt hdfs://10.10.1.1:9000/output/part3_t1_output
end=`date +%s`
echo runtime=$((end-start)) >> part3_t2_small.log