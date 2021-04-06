from rest_framework import serializers

from posts.models import Post

class PostSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','content','timestamp']
        read_only = ['id','timestamp']
    