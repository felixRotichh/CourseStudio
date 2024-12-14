import helpers
from cloudinary import CloudinaryImage
from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import Course, Lesson

class LessonInline(admin.StackedInline):
    model = Lesson
    readonly_fields = ['public_id','updated', 'display_image']
    extra = 0

    def display_image(self, obj, *args,**kwargs):
        url = helpers.get_cloudinary_image_object(
            obj, 
            field_name='thumbnail', 
            width=200)
       
        return format_html(f"<img src={url} />")
    
    display_image.short_description = "Current image"


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ['title', 'status', 'access']
    list_filter = ['status', 'access']
    fields = ['public_id','title', 'description', 'status', 'image', 'access', 'display_image']
    readonly_fields = ['display_image','public_id']

    
    def display_image(self, obj, *args,**kwargs):
        url = obj.image_admin
       
        return format_html(f"<img src={url} />")
    
    display_image.short_description = "Current image"
        
#admin.site.register(Course)

