import json
import boto3
import uuid

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    for record in event['Records']:
        # Extract message from SNS
        message = json.loads(record['Sns']['Message'])
        transaction_id = message['transaction_id']
        
        # Transform data (e.g., add a processed flag)
        transformed_data = {
            'transaction_id': transaction_id,
            'product_id': message['product_id'],
            'quantity': message['quantity'],
            'price': message['price'],
            'region': message['region'],
            'timestamp': message['timestamp'],
            'processed': True
        }
        
        # Define S3 bucket and key
        bucket_name = 'sales-data-bucket-asattar'  # Replace with your bucket name
        s3_key = f'transformed/sales_{transaction_id}.json'
        
        # Upload to S3
        s3_client.put_object(
            Bucket=bucket_name,
            Key=s3_key,
            Body=json.dumps(transformed_data)
        )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully processed SNS message')
    }