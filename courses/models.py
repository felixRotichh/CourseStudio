from django.db import models

# Create your models here.
'''
Course:
    - title
    - description
    - image/thumbnail
    -access:
        - anyone
        - email required
        -purchase required
        -user required(n/a)
    -Status:
        -draft
        -review/coming soon
        -published
    -
    - created_at
    - updated_at
'''
class PublishStatus(models.TextChoices):
    DRAFT = 'draft', 'Draft'
    COMING_SOON = 'coming_soon', 'Coming Soon'
    PUBLISHED = 'published', 'Published'

class AccessRequirement(models.TextChoices):
    ANYONE = 'anyone', 'Anyone'
    EMAIL_REQUIRED = 'email', 'Email Required'
    
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='courses/thumbnails/')
    access = models.CharField(
        max_length=15,
        choices=AccessRequirement.choices,
        default=AccessRequirement.ANYONE
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

