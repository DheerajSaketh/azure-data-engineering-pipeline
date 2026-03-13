from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df_raw = spark.read.parquet("/mnt/bronze/sample_clean")

df_transformed = (
    df_raw.withColumnRenamed("name", "customer_name")
          .withColumn("age_group",
                      when(df_raw.age < 30, "Young")
                      .otherwise("Adult"))
)

df_transformed.write.mode("overwrite").parquet("/mnt/silver/customer_transformed")