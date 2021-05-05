from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
# from django.utils.translation import 


image_storage = FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}/my_sell/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}my_sell/'.format(settings.MEDIA_URL),
)

def image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/my_sell/picture/<filename>
    return u'picture/{0}'.format(filename)

class HomeImageSlider(models.Model):
    image = models.FileField(upload_to=image_directory_path, storage=image_storage)

# class Table(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
    



# class Product(models.Model):
#     name = models.ForeignKey("Table",on_delete=models.CASCADE)
#     image = models.ImageField(upload_to=image_directory_path, height_field=None, width_field=None, max_length=None, storage=image_storage)
#     description = models.CharField(max_length=200)
#     title = models.CharField(max_length=100)
#     created_date = models.DateField(auto_now=False, auto_now_add=False)

#     def __str__(self):
#         return self.title
    
class AboutUs(models.Model):
    description = models.TextField()


class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name
    