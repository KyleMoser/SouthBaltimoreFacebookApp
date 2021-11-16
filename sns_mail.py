"""
Send an SNS (Simple Notification Service) email using the AWS library for Python (boto3)
"""

import boto3
from botocore.exceptions import ClientError

# This is the app developer address, it is also registered with Facebook.
SENDER = "Kyle Moser <southbaltimoreapps@gmail.com>"

# In the LIVE app this is replaced with the Facebook group/page owner email.
# This is done manually, the group/page owner gives the app developer the email they want to use.
# In development mode the app developer will receive the test messages.
RECIPIENT = "Kyle Moser <southbaltimoreapps@gmail.com>"

# Region we always use for AWS.
AWS_REGION = "us-east-1"

# The subject line for the email.
SUBJECT = "Facebook videos posted in the last %s days: "

# The email body for recipients with non-HTML email clients.
BODY_TEXT = "Links posted in the last %s days: "

# The HTML body of the email.
BODY_HTML = """<html>
<head></head>
<body>
  <h1>Facebook videos posted to the group {group} in the last {days} days</h1>
  <p>{links}</p>
</body>
</html>"""   

# The character encoding for the email.
CHARSET = "UTF-8"

def send_sns(group, days, video_list):
    """Send the SNS message that contains the list of video links posted to the facebook group or page"""
    # Create a new SES resource and specify a region.
    client = boto3.client('ses',region_name=AWS_REGION)
    BODY_HTML.format(group=group, days=days)
    vids = ""

    for video in video_list:
        vids = vids + "<a href='" + video + "'></a><br>"
        
    BODY_HTML.format(links=vids)

    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
    # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])