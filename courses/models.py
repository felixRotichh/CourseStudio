from django.db import models
import helpers
from django.utils.text import slugify
import uuid
from cloudinary.models import CloudinaryField

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

def get_public_id_prefix(instance,*args, **kwargs):
    title = instance.title
    if title:
        slug = slugify(title)
        unique_id = slugify(uuid.uuid4()).replace("-", "")[:5]
        return f"courses/{slug}-{unique_id}"
    if instance.id:
        return f"courses/{instance.id}"
    return "courses"

def get_display_name(instance,*args, **kwargs):
    title = instance.title
    if title:
        return title    
    return "Courses Upload"
    
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    #image = models.ImageField(upload_to=handle_upload, blank=True, null=True)
    image = CloudinaryField("image", null=True, 
                            public_id_prefix=get_public_id_prefix, 
                            display_name=get_display_name,
                            tags=["course","thumbnail"]
                            )
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
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED
    
    @property 
    def image_admin(self):
        if not self.image:
            return""
        image_options = {
            "width":200
        }
        url =  self.image.build_url(**image_options)
        return url
    
    def get_image_detail(self, as_html=False, width=750):
        if not self.image:
            return""
        image_options = {
            "width":200
        }

        if as_html:
            return self.image.image(**image_options)
        url =  self.image.build_url(**image_options)
        return
    
#Lesson.objects.alll() #lesson queryset -> all rows
#lesson.objects.first()
#course_obj = Course.objects.first()
#Lesson.objects.filter(course__id =course_obj.id)
#course_obj.lesson_set.all()
#lesson_obj = lesson.objects.first()

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    thumbnail = CloudinaryField("image", blank=True, null=True)
    video = CloudinaryField("video", blank=True, null=True, resource_type="video")
    order = models.IntegerField(default=0)
    can_preview = models.BooleanField(default=False, help_text="If user does not have access course, can they see this?" )
    status = models.CharField(
        max_length=15,
        choices=PublishStatus.choices,
        default=PublishStatus.PUBLISHED
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-updated']