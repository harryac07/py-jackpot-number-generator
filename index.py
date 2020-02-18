import json
import os
import boto3
import datetime

from utils.generate_numbers import JackpotGenerator

client = boto3.client('sesv2')


def handler(event, context):
    receiver = os.environ.get('SENDER_EMAIL')
    sender = os.environ.get('SENDER_EMAIL')
    # Supply jackpot specific min and max numbers
    # First 2 params => Main numbers, Last 2 numbers => Bonus numbers
    week_number = datetime.datetime.today().weekday()

    # If Friday, return for eurojackpot with bonus numbers
    # Else return without bonus numbers
    if week_number == 4:
        number_obj = JackpotGenerator(1, 50, 1, 10)
        number_obj.generate_numbers(5, 2)
    else:
        number_obj = JackpotGenerator(1, 42, 1, 10)
        number_obj.generate_numbers(5, 0)
    
    message_body = """
    <h3>Hello there!</h3>
    <p>Here are the numbers you can use to win Jackpot of your choice!</p>    
    {}
    <br/>
    <br/>
    Good Luck! &#x1F60E;
    """.format(number_obj)

    client.send_email(
        FromEmailAddress=sender,
        Destination={
            'ToAddresses': [
                receiver,
            ]
        },
        Content={
            'Simple': {
                'Subject': {
                    'Data': 'Its a Jackpot time. Good Luck!',
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Html': {
                        'Data': message_body,
                        'Charset': 'UTF-8'
                    }
                }
            }
        }
    )
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Message sent!"
        })
    }
    return response
