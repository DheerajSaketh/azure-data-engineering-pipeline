# Azure Data Engineering Pipeline

This project demonstrates an end-to-end data engineering pipeline on **Microsoft Azure** using:

- Azure Data Factory (ADF)
- Azure Databricks (PySpark)
- Azure Data Lake Storage (ADLS)
- Azure Synapse Analytics
- Power BI

## 🧱 Architecture

1. **Ingestion:** Raw data is ingested into ADLS (Bronze layer) using ADF.
2. **Transformation:** Databricks notebooks clean and transform data into Silver and Gold layers.
3. **Serving:** Curated data is loaded into Synapse for analytics and reporting.
4. **Visualization:** Power BI dashboards consume Synapse data for business insights.

## 🛠 Tech Stack

- **Languages:** Python, SQL, PySpark  
- **Azure Services:** ADF, Databricks, ADLS, Synapse, Key Vault  
- **Other:** Git, Azure DevOps (for CI/CD)

## 🚧 Status

This project is a **work in progress**. Code, notebooks, and pipeline definitions will be added soon.
