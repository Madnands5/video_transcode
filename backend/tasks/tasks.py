import os
import subprocess
from celery import shared_task
from django.conf import settings
from .models import VideoTask
from config.services.s3_service import S3Service
from config.services.email_service import EmailService

@shared_task
def transcode_video_task(task_id):
    task = VideoTask.objects.get(id=task_id)
    task.status = 'PROCESSING'
    task.save()
    
    s3 = S3Service.get_client()
    local_input = f"/tmp/{task.id}_input.mp4"
    local_output = f"/tmp/{task.id}_output.mp4"
    
    try:
        # 1. Download
        s3.download_file(settings.AWS_STORAGE_BUCKET_NAME, task.input_file_key, local_input)
        
        # 2. Transcode
        subprocess.run(['ffmpeg', '-i', local_input, local_output], check=True)
        
        # 3. Upload
        output_key = f"processed/{task.id}.mp4"
        s3.upload_file(local_output, settings.AWS_STORAGE_BUCKET_NAME, output_key)
        s3.delete_object(
            Bucket=settings.AWS_STORAGE_BUCKET_NAME, 
            Key=task.input_file_key
        )
        # 4. Success
        task.status = 'COMPLETED'
        EmailService.send_notification("Success", f"Video {task.id} is ready.")
        delete_processed_file_task.apply_async(
        args=[output_key], 
        countdown=1800
        )
        
    except Exception as e:
        task.status = 'FAILED'
        # Log the error here
    finally:
        # 5. Cleanup
        if os.path.exists(local_input): os.remove(local_input)
        if os.path.exists(local_output): os.remove(local_output)
        task.save()

@shared_task
def delete_processed_file_task(s3_key):
    """Deletes a file from S3 after a delay."""
    s3 = S3Service.get_client()
    try:
        s3.delete_object(
            Bucket=settings.AWS_STORAGE_BUCKET_NAME, 
            Key=s3_key
        )
    except Exception as e:
        # Log error: could not delete file
        pass