from django.db import models
import helpers

helpers.cloudinary_init()

class PublishStatus(models.TextChoices):
    DRAFT = 'draft', 'Draft'
    COMING_SOON = 'coming_soon', 'Coming Soon'
    PUBLISHED = 'published', 'Published'

class AccessRequirement(models.TextChoices):
    ANYONE = 'anyone', 'Anyone'
    EMAIL_REQUIRED = 'email', 'Email Required'


def handle_upload(instance, filename):
    return f"{filename}"
    
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=handle_upload,
                              blank=True, null=True)
    access = models.CharField(
        max_length=35,
        choices=AccessRequirement.choices,
        default=AccessRequirement.EMAIL_REQUIRED
    )
    status = models.CharField(
        max_length=15,
        choices=PublishStatus.choices,
        default=PublishStatus.DRAFT
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED

