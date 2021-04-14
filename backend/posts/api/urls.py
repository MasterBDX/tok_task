from django.urls import path

from .views import (PostsAPIView,
                    AddPostAPIView,
                    PostDetailAPIView,
                    PostUpdateAPIView,
                    PostDeleteAPIView)


app_name = 'posts.api'
urlpatterns = [
    path('',PostsAPIView.as_view(),name='list'),
    path('add/',AddPostAPIView.as_view(),name='add'),
    path('<int:pk>/',PostDetailAPIView.as_view(),name='Detail'),
    path('<int:pk>/update/',PostUpdateAPIView.as_view(),name='update'),
    path('<int:pk>/delete/',PostDeleteAPIView.as_view(),name='delete'),   
]

