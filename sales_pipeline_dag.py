from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime, timedelta
import boto3
from snowflake.connector import connect

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'sales_pipeline',
    default_args=default_args,
    description='A pipeline to process sales data from SNS to Snowflake via Lambda and S3',
    schedule_interval=timedelta(days=1),  # Runs daily; adjust as needed
    start_date=datetime(2025, 6, 27),
    catchup=False,
) as dag:

    # Function to trigger Lambda (simulated)
    def trigger_lambda():
        lambda_client = boto3.client('lambda', region_name='us-east-1')  # Adjust region
        lambda_client.invoke(
            FunctionName='SalesTransformer',
            InvocationType='Event'
        )
        print("Lambda triggered successfully.")

    # Function to copy data from S3 to local (simulated)
    def copy_from_s3():
        s3_client = boto3.client('s3', region_name='us-east-1')  # Adjust region
        bucket_name = 'sales-data-bucket-asattar '
        file_key = 'sales_data.csv'  # Adjust file name
        s3_client.download_file(bucket_name, file_key, '/tmp/sales_data.csv')
        print("Data copied from S3.")

    # Function to load data into Snowflake (simulated)
    def load_to_snowflake():
        conn = connect(
            user='asbrohi',
            password='CV3j759tnXRZpvg',
            account='oqc97332.us-east-1',  # e.g., 'xy12345.us-east-1'
            warehouse='COMPUTE_WH',
            database='SALES_DB',
            schema='SALES_SCHEMA'
        )
        cursor = conn.cursor()
        cursor.execute("COPY INTO your_table FROM @your_stage/sales_data.csv")
        conn.close()
        print("Data loaded into Snowflake.")

    # Define tasks
    start_task = DummyOperator(task_id='start')

    trigger_lambda_task = PythonOperator(
        task_id='trigger_lambda',
        python_callable=trigger_lambda,
    )

    copy_s3_task = PythonOperator(
        task_id='copy_from_s3',
        python_callable=copy_s3,
    )

    load_snowflake_task = PythonOperator(
        task_id='load_to_snowflake',
        python_callable=load_to_snowflake,
    )

    end_task = DummyOperator(task_id='end')

    # Define task dependencies
    start_task >> trigger_lambda_task >> copy_s3_task >> load_snowflake_task >> end_task