from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.read.csv("/mnt/raw/sample.csv", header=True)

df_clean = df.dropna()

df_clean.write.mode("overwrite").parquet("/mnt/silver/sample_clean")