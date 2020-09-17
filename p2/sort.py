from pyspark.sql import SparkSession
import sys

if __name__ == '__main__':
    # Check args
    # Show is a helper function just to be able to print the head of a csv file
    show = False
    if len(sys.argv) != 3:
        print('Usage: sort INPUT_FILE OUTPUT_FILE')
        print('Alterative usage: sort --show CSV')

    if sys.argv[1] == '--show':
        show = True

    inp = sys.argv[1]
    out = sys.argv[2]
    spark = SparkSession.builder.master("local[*]").appName('sort').getOrCreate() # Instantiate session
    if show: # Quick helper just to examine output
        df = spark.read.csv(out, header=False)
        df.show(10)
    else: # Actual sort function
        df = spark.read.csv(inp, header=True)
        df = df.orderBy(['cca2', 'timestamp'], ascending=[True, True]) # Sort by ascending, in correct ordre
        df.coalesce(1).write.csv(out) # Write output

