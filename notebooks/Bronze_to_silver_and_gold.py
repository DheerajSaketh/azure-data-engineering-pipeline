from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, sum as _sum, count as _count

spark = SparkSession.builder.getOrCreate()

# -------------------------
# Bronze → Silver
# -------------------------
df_bronze = spark.read.csv("/mnt/raw/sample.csv", header=True, inferSchema=True)

df_silver = (
    df_bronze
    .dropna()
    .withColumn("age_group",
                when(col("age") < 30, "Young")
                .otherwise("Adult"))
)

df_silver.write.format("delta").mode("overwrite").save("/mnt/silver/customer_clean")

# -------------------------
# Silver → Gold
# -------------------------
df_gold = (
    df_silver.groupBy("age_group")
    .agg(
        _count("*").alias("total_customers"),
        _sum("age").alias("total_age")
    )
)

df_gold.write.format("delta").mode("overwrite").save("/mnt/gold/customer_summary")