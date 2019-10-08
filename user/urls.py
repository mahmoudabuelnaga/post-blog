from django.urls import path, include
from .views import User_register
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', User_register.as_view(), name='register'),
]