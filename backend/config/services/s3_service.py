import boto3
from django.conf import settings

class S3Service:
    @staticmethod
    def get_client():
        """Initializes the S3 client based on environment configuration."""
        client_args = {
            'aws_access_key_id': settings.AWS_ACCESS_KEY_ID,
            'aws_secret_access_key': settings.AWS_SECRET_ACCESS_KEY,
            'region_name': settings.AWS_REGION
        }
        
        # If running in local dev mode with LocalStack
        if getattr(settings, 'USE_LOCALSTACK', False):
            client_args['endpoint_url'] = settings.LOCALSTACK_ENDPOINT_URL
            
        return boto3.client('s3', **client_args)

    @classmethod
    def generate_upload_url(cls, file_key):
        """Generates a pre-signed URL for S3/LocalStack uploads."""
        client = cls.get_client()
        return client.generate_presigned_url(
            'put_object',
            Params={
                'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
                'Key': file_key,
                'ContentType': 'video/mp4'
            },
            ExpiresIn=3600
        )