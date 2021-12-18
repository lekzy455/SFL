from django.urls import path
from .views import UserRegistrationAPIView

app_name = "authentication"

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    # path('login/', LoginAPIView.as_view(), name='login'),
]
