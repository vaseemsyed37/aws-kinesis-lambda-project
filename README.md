# AWS Kinesis & Lambda Log Processing 🚀

This project demonstrates real-time log processing using **AWS Kinesis** and **AWS Lambda**.

## 🔹 Features:
- Streams data using **Amazon Kinesis**
- Processes logs using **AWS Lambda**
- Stores logs in **CloudWatch**
- Uses **IAM roles** for security

## 🔹 Technologies Used:
- AWS Kinesis
- AWS Lambda
- Python (Boto3)
- CloudWatch Logs

## 🔹 How It Works:
1. A data producer sends logs to the **Kinesis stream**.
2. The **Lambda function** reads the stream and processes the logs.
3. The processed logs are stored in **CloudWatch Logs** for monitoring.

## 🔹 Setup Instructions:
1. Clone this repository:
   ```sh
   git clone https://github.com/vaseemsyed37/aws-kinesis-lambda-project.git
   cd aws-kinesis-lambda-project
   ```
2. Deploy the **Lambda function**:
   - Upload `lambda_function.py` to AWS Lambda.
   - Set execution role with **Kinesis & CloudWatch** permissions.

3. Create a **Kinesis Stream** and connect it to Lambda.

4. Send test data:
   ```sh
   aws kinesis put-record --stream-name log-stream-project --partition-key test-key --data "Test log entry"
   ```

## 🔹 Expected Output:
- The Lambda function processes log entries in real-time.
- Logs appear in **CloudWatch**.

