from rest_framework.generics import ( ListAPIView,
                                      CreateAPIView,
                                      RetrieveAPIView,
                                      UpdateAPIView,
                                      DestroyAPIView)
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model

User = get_user_model()

from .serializers import PostSerailizer,AddPostSerializer
from posts.models import Post

class PostsAPIView(ListAPIView):
    serializer_class  = PostSerailizer
    queryset = Post.objects.all()
    

class PostDetailAPIView(RetrieveAPIView):
    serializer_class  = PostSerailizer
    queryset = Post.objects.all()


class AddPostAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AddPostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostUpdateAPIView(UpdateAPIView):
    serializer_class  = PostSerailizer
    queryset = Post.objects.all()

class PostDeleteAPIView(DestroyAPIView):
    serializer_class  = PostSerailizer
    queryset = Post.objects.all()


