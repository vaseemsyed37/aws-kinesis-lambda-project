import json
import boto3
import base64

# Initialize AWS Kinesis client
kinesis_client = boto3.client("kinesis", region_name="us-east-1")

# Define the Kinesis stream name
KINESIS_STREAM_NAME = "log-stream-project"

def lambda_handler(event, context):
    for record in event['Records']:
        # Decode base64 encoded data from Kinesis
        payload = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        
        # Convert string to JSON object
        log_data = json.loads(payload)
        
        # Print the received log data
        print(f"Received log data: {log_data}")

        # Send cleaned-up data to Kinesis
        response = kinesis_client.put_record(
            StreamName=KINESIS_STREAM_NAME,
            Data=json.dumps({"timestamp": log_data["timestamp"], "message": log_data["message"]}),
            PartitionKey="test-key"
        )

        print(f"Data sent to Kinesis: {response}")

    return {
        'statusCode': 200,
        'body': json.dumps('Log processing and re-ingestion complete!')
    }

