# Sales ETL Pipeline Automation

## Overview
This project implements an automated Extract, Transform, Load (ETL) pipeline to process mock retail sales data (e.g., electronic product transactions) and enable real-time analytics. The pipeline leverages AWS services, Snowflake, Apache Airflow, and Power BI to ingest, transform, and visualize over 999+ JSON files.

## Project Status
- **Active Development**: Currently ingesting data, transforming raw files, orchestrating workflows, and visualizing insights.
- **Start Date**: May 2025
- **Status**: Ongoing

## Architecture
- **Local Script**: Generates mock sales data as JSON files.
- **AWS SNS**: Notifies the pipeline of new data.
- **AWS Lambda**: Processes events and manages data flow.
- **Raw Data S3**: Stores initial JSON files.
- **Transformed Data S3**: Stores processed JSON files.
- **Snowpipe**: Ingests data from S3 into Snowflake.
- **Snowflake**: Hosts the sales data warehouse.
- **EC2 with Airflow**: Orchestrates the ETL process.
- **Power BI**: Visualizes real-time sales analytics.

### Data Flow
1. Local Script → SNS: Initial JSON Notification
2. SNS → Lambda: Event Processing Trigger
3. Lambda → Raw Data S3: Raw JSON Upload
4. Raw Data S3 → Lambda: Transformation Request
5. Lambda → Transformed Data S3: Processed JSON Storage
6. Transformed Data S3 → Snowpipe: Ingestion Request
7. Snowpipe → Snowflake: Data Loading
8. EC2 with Airflow → Snowflake: Orchestration Query
9. Snowflake → Power BI: Real-Time Visualization Data

## Technologies
- **AWS**: SNS, Lambda, S3
- **Snowflake**: Data warehousing
- **Apache Airflow**: Workflow orchestration (on EC2)
- **Power BI**: Data visualization
- **Python**: Scripting (e.g., `publish_sales_to_sns.py`)

## Setup and Usage
1. **Prerequisites**:
   - AWS account with SNS, Lambda, and S3 configured.
   - Snowflake account with Snowpipe and a warehouse.
   - EC2 instance with Airflow installed.
   - Power BI Desktop installed.
2. **Configuration**:
   - Update `publish_sales_to_sns.py` with your S3 bucket and SNS topic.
   - Configure Lambda to trigger on SNS and process S3 files.
   - Set up Snowpipe to ingest from Transformed Data S3.
   - Deploy Airflow DAG on EC2 to monitor the pipeline.
   - Connect Power BI to Snowflake with Direct Query.
3. **Run**:
   - Execute `publish_sales_to_sns.py` to generate and upload JSON files.
   - Monitor ingestion via Snowpipe and visualize in Power BI.

## Achievements
- Successfully processed over 999+ JSON files.
- Enabled real-time analytics for mock retail sales data.
- Documented in a Lucidchart architecture diagram (`sales_pipeline_architecture`).

## Future Improvements
- Automate data transformation logic in Lambda.
- Add error handling and logging.
- Expand visualization dashboards in Power BI.

## License
[MIT License](https://opensource.org/licenses/MIT) (or specify your preferred license).

## Contact
For questions or contributions, contact [Your Name/Email] (update with your details).