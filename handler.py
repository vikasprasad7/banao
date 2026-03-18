import json

def send_email(event, context):
    body = json.loads(event['body'])
    # In production, use AWS SES or SendGrid here
    print(f"Mock email sent to {body['email']}: Welcome {body['role']} {body['username']}!")
    
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Email triggered successfully"})
    }
