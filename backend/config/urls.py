from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This will include all URLs from your 'tasks' app later
    path('api/tasks/', include('tasks.urls')), 
]