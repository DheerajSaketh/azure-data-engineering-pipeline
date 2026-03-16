# Power BI Dashboard

This folder contains Power BI assets for the Azure Data Engineering Pipeline project.

## 📊 Dashboard Overview
The dashboard visualizes:

- Customer age distribution
- Total customers by age group
- Total spending metrics
- Data quality checks
- Pipeline run status (optional)

## 📁 Files to Upload Later
- `customer_summary.pbix` (Power BI report)
- `dataset_definition.json` (Power BI dataset metadata)
- `data_model.png` (Star schema diagram)

## 📝 Instructions
1. Connect Power BI to Synapse SQL Serverless or Dedicated Pool.
2. Import the `gold.customer_summary` table.
3. Build visuals:
   - Bar chart: Customers by age group
   - KPI: Total customers
   - KPI: Total age sum
4. Save the report as `.pbix` and upload it here.

## Dataset Definition
The `dataset_definition.json` provides the schema for connecting to Synapse.

## Best Practices

- Use DirectQuery for real-time data
- Implement row-level security
- Create shared datasets for consistency
- Use Power BI dataflows for additional transformations
- Publish to Power BI Service for sharing
