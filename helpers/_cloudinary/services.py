

def get_cloudinary_image_object(instance,
                                as_html=False,
                                width=1200,
                                 field_name="image"):
    if not hasattr(instance, field_name):
          return ""
    image_object = getattr(instance, field_name)

    if not image_object:
            return ""
    image_options = {
            "width":width
        }
    if as_html:
          return instance.image.image(**image_options)
    url =  instance.image.build_url(**image_options)
    return url