from django.contrib import admin
import logging
from django.utils.safestring import mark_safe

# Register your models here.
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'access']
    list_filter = ['status', 'access']
    fields = ['title', 'description', 'status', 'image', 'access', 'display_image']
    readonly_fields = ['display_image']

    logger = logging.getLogger(__name__)
    
    def display_image(self, obj, *args,**kwargs):
        url = obj.image.url if obj.image else ''  # Check if image exists
        logger.debug(f"Image URL: {url}")  # Log the URL for debugging
        if not url:
            return "No image available"  # Return a message if no image
        return mark_safe(f"<img src='{url}' style='max-width: 100px;'/>")  # Use mark_safe to render HTML
#admin.site.register(Course)

