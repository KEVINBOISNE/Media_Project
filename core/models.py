#from django.contrib.auth.models import AbstractUser
#from django.db import models
# Create your models here.
# class CustomUser(AbstractUser):
#     ROLE_ADMIN = 'admin'
#     ROLE_MEDIA_OPERATOR = 'media_operator'
#     ROLE_VIEWER = 'viewer'

#     ROLE_CHOICES = (
#         (ROLE_ADMIN, 'Admin'),
#         (ROLE_MEDIA_OPERATOR, 'Media Operator'),
#         (ROLE_VIEWER, 'Viewer'),
#     )

#     role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_VIEWER )

from django.db import models
import uuid # To have unique ID and not 1234...

"""
 class MediaFile
    
Settings : models.Model
Goal : Stock media informations in PSQL Table
"""
class MediaFile(models.Model):
    """
    class JobStatus
         
Settings : models.TextChoices ( type enumerate from Django )
Goal : Stock media informations in PSQL Table too"""
class JobStatus(models.TextChoices):
   PENDING = "pending", "Pending"
   PROCESSING = "processing", "Processing"
   DONE = "done", "Done"
   FAILED = "failed", "Failed"

id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
file_name = models.TextField()
file_type = models.CharField(
max_length=50,
    choices=[("image", "Image"), ("video", "Video"), ("other", "Other")],
    default="other"
        )
url = models.URLField()
size = models.BigIntegerField(null=True, blank=True)
meta_data = models.BooleanField(default=False)

job_status = models.CharField(
    max_length=20,
    choices=JobStatus.choices,
    default=JobStatus.PENDING
        )
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)