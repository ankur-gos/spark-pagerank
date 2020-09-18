for i in $(seq 100 200 500)
do
    hdfs dfs -rm -r /output/part3_t2_output
    echo Run small with partition number $i
    start=`date +%s`
    /users/yunjia/spark-2.4.7-bin-hadoop2.7/bin/spark-submit part3_t2_spark_pagerank.py spark://172.16.86.1:7077 hdfs://10.10.1.1:9000/input/*xml* hdfs://10.10.1.1:9000/output/part3_t2_output $i 2>  part3_t2_large.log
    # python3 part3_spark_pagerank.py local ./data/part3/web-BerkStan.txt hdfs://10.10.1.1:9000/output/part3_t1_output
    end=`date +%s`
    echo runtime=$((end-start)) >> part3_t2_large.log
done
