from django.contrib import admin
from django.urls import path, include
from apps.account.views import UserDataView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('apps.account.urls')),
    path('user/<int:user_id>/', UserDataView.as_view()),
]
