from django.urls import path
from . import views
from site_2_process_instrument import views

urlpatterns = [
    
    path('', views.home,name="Home"),
    path('about/', views.about,name="About"),
    path('contact/', views.contact, name="Contact"),
    path('mega/',views.mega,name="Mega"),
    path('product_category/',views.product_category,name="product_category")
]
        