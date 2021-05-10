from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.validators import MaxValueValidator
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

#site 2 home page image slider model
class HomeImageSlider(models.Model):
    image             = models.FileField(upload_to=image_directory_path, storage=image_storage,help_text='Enter image you want to display on the home page slider ')
    image_description = models.CharField(max_length=250,help_text='Enter image description')
    image_heading     = models.CharField(max_length=250,help_text='Enter image Heading')

#site 2 home page counts model
class HomePageData(models.Model):
    TechnicalStaff          = models.IntegerField()
    YearsOfExperience       = models.IntegerField(validators=[MaxValueValidator(99)])
    NumberOfSatisfiedClient = models.IntegerField()
    StatesCoveredInIndia    = models.IntegerField(validators=[MaxValueValidator(29)])
 
class InstrumentsParametersWise(models.Model):
    title           = models.CharField(max_length=100,help_text='Enter <b>Title of "InstrumentsParametersWise"</b> which is displyed on home page ')
    description     = models.CharField(max_length=500,help_text='Enter <b>Description of "Title of InstrumentsParametersWise"</b> which is displyed on home page ')
    bootstrap_icons = models.CharField(max_length=100,help_text='<h4>do not play with this, this part is related to coding </h4>',blank=True)

    def __str__(self):
        return self.title
    

#site 2 aboutus page description model
class AboutUs(models.Model):
    description = models.TextField(help_text='enter description of the about us page.' )

#site 2 contactus page  which gather data from forms and store in models.
class ContactModel(models.Model):
    name    = models.CharField(max_length=50)
    email   = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name

#site 2 contactus page display contact information
class Contact_display(models.Model):                                                                
    display_location = models.CharField(max_length=100, help_text='Enter your <b>LOCATION</b> which will be display on contact form')
    display_email    = models.EmailField(max_length=254, help_text='Enter your <b>EMAIL</b> which will be display on contact form')
    display_call     = models.CharField(max_length=100, help_text='Enter your <b>PHONE_NUMBER</b> which will be display on contact form')

    def __str__(self):
        return self.display_email
    



 # ------------------------------------------------------------------------------------------------------------
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