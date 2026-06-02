import boto3
from django.conf import settings

class EmailService:
    @staticmethod
    def get_client():
        return boto3.client(
            'sns',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION
        )

    @classmethod
    def send_notification(cls, subject, message):
        client = cls.get_client()
        # You will need your SNS Topic ARN in your .env
        client.publish(
            TopicArn=settings.AWS_SNS_TOPIC_ARN,
            Subject=subject,
            Message=message
        )