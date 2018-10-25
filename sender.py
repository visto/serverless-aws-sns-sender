import json
import boto3

from flask import Flask, jsonify
app = Flask(__name__)

# @app.route("/send", methods=["POST"])
def send(event, context):
    data = json.loads(event['body'])
    phone_number = data['Where']
    title = data['Title']
    message = data['Description'] + " " + title
    if not phone_number or not title or not message:
        return jsonify({'error': 'Please provide phone number, title, and message'}), 400
    
    
    # Create an SNS client
    client = boto3.client(
        "sns",
        aws_access_key_id="S0MEF4NCPEACEKEY",
        aws_secret_access_key="s0MEFANCY/S3CR3t/keykey",
        region_name="us-east-1"
    )

    # Send your sms message.
    client.publish(
        PhoneNumber=phone_number,
        Message=message
    )

    response = {
        "statusCode": 200,
        "body": json.dumps("Your message was sent successfully")
    }

    return response