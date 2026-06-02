from django.db import models
import uuid

class VideoTask(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()
    dimension = models.CharField(max_length=10)  # e.g., '1080p', '720p'
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    input_file_key = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.status}"