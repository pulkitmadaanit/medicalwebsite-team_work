from django.contrib import admin
from django.urls import path , include

# from scienco_india_solutions import views

# Setting and static file
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_page.urls')),
    path('site1_printing/', include('site_1_printing_advertisement.urls')),
    path('site2_instruments/', include('site_2_process_instrument.urls')),
        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



