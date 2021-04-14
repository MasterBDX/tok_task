from django.urls import path
from .views import UserLoginAPIView

app_name = 'accounts.api'
urlpatterns = [
    path('login/',UserLoginAPIView.as_view(),name='login')
]

