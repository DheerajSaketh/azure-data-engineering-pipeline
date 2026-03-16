# Deployment

This folder contains ARM templates and scripts for deploying the Azure Data Engineering Pipeline.

## ARM Templates

- `storage_template.json`: Deploys Azure Data Lake Storage Gen2 account.

## Deployment Steps

1. Create a resource group in Azure.
2. Deploy the storage account using the ARM template.
3. Create Databricks workspace, Data Factory, Synapse workspace manually or via additional templates.
4. Configure linked services in ADF to point to the storage and Databricks.
5. Upload notebooks to Databricks.
6. Import pipeline JSONs into ADF.
7. Run the pipeline.

## Parameters

For storage_template.json:
- storageAccountName: Unique name for the storage account.