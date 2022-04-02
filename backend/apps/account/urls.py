from django.urls import path
from .views import MyObtainTokenPairView, RegisterView, Welcome
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('welcome/', Welcome.as_view()),
    path('signup/', RegisterView.as_view(), name='register'),

    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]