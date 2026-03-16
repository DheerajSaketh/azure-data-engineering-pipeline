# Azure Synapse Analytics

This folder contains SQL scripts for Azure Synapse Analytics.

## Files

- `gold_table.sql`: Creates external table for Gold layer data

## Usage

1. Execute the SQL in Synapse Studio or SQL Serverless
2. Update the LOCATION path to your ADLS Gold container
3. Create additional views or tables as needed

## SQL Details

### Gold Table
- Uses Delta format for external table
- Points to aggregated customer summary data
- Enables serverless querying

## Best Practices

- Use external tables for data lake access
- Implement row-level security if needed
- Create materialized views for performance
- Use Synapse pipelines for data loading
- Monitor query performance and optimize
