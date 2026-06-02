import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import VideoTask
from config.services.s3_service import S3Service  # Your centralized service

class GenerateUploadURLView(APIView):
    def post(self, request):
        email = request.data.get('email')
        dimension = request.data.get('dimension')

        if not email or not dimension:
            return Response(
                {"error": "Missing email or dimension"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        # 1. Save to Database
        file_key = f"uploads/{uuid.uuid4()}.mp4"
        task = VideoTask.objects.create(
            email=email, 
            dimension=dimension, 
            input_file_key=file_key
        )

        # 2. Generate S3 Pre-signed URL using the Service Layer
        # This automatically handles AWS vs. LocalStack based on settings
        upload_url = S3Service.generate_upload_url(file_key)

        return Response({
            'url': upload_url, 
            'task_id': task.id
        }, status=status.HTTP_201_CREATED)