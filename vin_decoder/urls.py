from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('decoder.urls')),  # Include the decoder app's URLs
]
