import json
import boto3

def send_email(source, to, region, subject, body):
    client = boto3.client('ses', region_name=region)

    response = client.send_email(
        Source=source,
        Destination={
            'ToAddresses': [
                to,
            ]
        },
        Message={
            'Subject': {
                'Data': subject,
            },
            'Body': {
                'Text': {
                    'Data': body,
                },
            }
        }
    )
    
    return response

def lambda_handler(event, context):
    sender_mail  = event['sender_mail']
    receive_mail = event['receive_mail']
    region       = event['region']
    subject      = event['subject']
    body         = event['body']
    
    send_email_to = send_email(sender_mail, receive_mail, region, subject, body)
    print("Send ResponseMetadata:" + json.dumps(send_email_to, ensure_ascii=False))
    return {'send_email': 'success'}
