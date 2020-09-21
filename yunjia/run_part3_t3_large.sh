hdfs dfs -rm -r /output
start=`date +%s`
/users/yunjia/spark-2.4.7-bin-hadoop2.7/bin/spark-submit part3_t3_spark_pagerank.py spark://172.16.86.1:7077 /proj/uwmadison744-f20-PG0/data-part3/enwiki-pages-articles/ hdfs://10.10.1.1:9000/output/ 2> part3_t3_large.log
# # python3 part3_spark_pagerank.py local ./data/part3/web-BerkStan.txt hdfs://10.10.1.1:9000/output/part3_t1_output
end=`date +%s`
echo runtime=$((end-start)) >> part3_t3_large.log