from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('resume/', include('apps.resume.urls')),
    path('', include('apps.account.urls')),
]
