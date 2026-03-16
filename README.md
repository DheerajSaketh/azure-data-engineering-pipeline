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

## � Getting Started

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Test locally: `python scripts/local_test.py`
4. Deploy to Azure using ARM templates in `deploy/`.
5. Configure Azure services and run the pipeline.

## 📁 Project Structure

- `adf/`: Azure Data Factory pipeline definitions
- `data/`: Sample data files
- `deploy/`: ARM templates for deployment
- `docs/`: Architecture diagrams and documentation
- `notebooks/`: Databricks PySpark notebooks
- `powerbi/`: Power BI dataset definitions
- `scripts/`: Local testing scripts
- `synapse/`: Synapse SQL scripts
