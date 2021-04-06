from rest_framework.generics import ( ListAPIView,
                                      RetrieveAPIView,
                                      UpdateAPIView,
                                      DestroyAPIView)

from .serializers import PostSerailizer
from posts.models import Post

class PostsAPIView(ListAPIView):
    serializer_class  = PostSerailizer
    queryset = Post.objects.all()
    

class PostDetailAPIView(RetrieveAPIView):
    serializer_class  = PostSerailizer
    queryset = Post.objects.all()

class PostUpdateAPIView(UpdateAPIView):
    serializer_class  = PostSerailizer
    queryset = Post.objects.all()

class PostDeleteAPIView(DestroyAPIView):
    serializer_class  = PostSerailizer
    queryset = Post.objects.all()
