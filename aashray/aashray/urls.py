"""aashray URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('donor/',views.donate_plasma, name='donate_plasma'),
    path('hospital_beds/',views.hospital_beds, name='hospital_beds'),
    path('hospital_beds_data/',views.hospital_beds_data, name='hospital_beds_data'),
    path('medicines/',views.medicines, name='medicines_beds'),
    path('medicines_data/',views.medicines_data, name='medicines_data'),
    path('oxygen/',views.oxygen, name='oxygen_beds'),
    path('oxygen_data/',views.oxygen_data, name='oxygen_data'),
    path('plasma/',views.plasma, name='plasma_beds'),
    path('plasma_data/',views.plasma_data, name='plasma_data'),
    path('others/',views.others, name='others'),
    path('helplines/',views.helplines, name='helplines'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
