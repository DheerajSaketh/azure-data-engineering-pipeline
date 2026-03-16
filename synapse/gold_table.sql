CREATE EXTERNAL TABLE gold.customer_summary
(
    age_group STRING,
    total_customers BIGINT,
    total_age BIGINT
)
USING DELTA
LOCATION 'abfss://gold@<storage_account>.dfs.core.windows.net/customer_summary';