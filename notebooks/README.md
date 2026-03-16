# Databricks Notebooks

This folder contains PySpark notebooks for data processing in Azure Databricks.

## Files

- `Bronze_to_silver_and_gold.py`: Complete pipeline from Bronze to Gold layers
- `sample_notebook.py.py`: Basic data reading example
- `silver_transformation.py`: Silver layer transformation logic

## Usage

1. Import these notebooks into your Databricks workspace
2. Mount ADLS using Databricks secrets or service principals
3. Update mount paths (`/mnt/...`) to match your storage account
4. Run notebooks in sequence: Bronze → Silver → Gold

## Notebook Details

### Bronze to Silver and Gold
- Reads CSV from Bronze layer
- Applies data cleansing (drop nulls)
- Creates age groups
- Aggregates customer metrics for Gold layer
- Uses Delta format for ACID transactions

## Best Practices

- Use Delta Lake for reliable data storage
- Implement schema enforcement
- Add data quality checks
- Use Databricks jobs for orchestration
- Enable cluster autoscaling for cost optimization
