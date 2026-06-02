# project_root/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This line tells Django to look for 'api/' and send it to your app's urls
    path('api/', include('tasks.urls')), 
]