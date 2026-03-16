# Azure Data Factory

This folder contains Azure Data Factory pipeline definitions and configurations.

## Files

- `adf_pipeline.json`: Basic copy pipeline template
- `adf_pipeline_ingest_raw_to_bronze.json`: Pipeline for ingesting raw CSV data into Bronze layer (Parquet format)

## Usage

1. Import these JSON files into your ADF instance
2. Configure linked services for:
   - Source data (e.g., Azure Blob Storage, HTTP, etc.)
   - Sink: Azure Data Lake Storage Gen2
3. Update dataset references to match your environment
4. Schedule the pipeline or trigger manually

## Pipeline Details

### Ingest Raw to Bronze
- **Source**: Delimited text (CSV)
- **Sink**: Parquet format in ADLS Bronze container
- **Activities**: Single Copy activity with optional data flow transformations

## Best Practices

- Use parameterized datasets for reusability
- Implement error handling and logging
- Add triggers for scheduled execution
- Monitor pipeline runs in ADF monitoring hub
