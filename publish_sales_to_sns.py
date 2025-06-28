import json
import boto3
import time
import random

#debugging 
session = boto3.Session()
credentials = session.get_credentials()
print(credentials)  # Should print credential details if found
sns_client = boto3.client('sns', region_name='us-east-1')

# Initialize SNS client
sns_client = boto3.client('sns', region_name='us-east-1')
topic_arn = 'arn:aws:sns:us-east-1:006043185824:sales-topic'  # Replace with your topic ARN

def generate_sale():
    return {
        'transaction_id': random.randint(1000, 9999),
        'product_id': random.randint(1, 50),
        'quantity': random.randint(1, 10),
        'price': round(random.uniform(5.0, 100.0), 2),
        'region': random.choice(['US', 'EU', 'ASIA']),
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
    }

while True:
    sale = generate_sale()
    sns_client.publish(
        TopicArn=topic_arn,
        Message=json.dumps(sale)
    )
    print(f"Published: {sale}")
    time.sleep(1)  # Simulate real-time data