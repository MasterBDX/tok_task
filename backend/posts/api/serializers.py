from rest_framework import serializers

from posts.models import Post
from accounts.api.serializers import PostUserSerializer


class PostSerailizer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    timestamp = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id','user','content','timestamp']
        read_only = ['timestamp']
    
    def get_user(self,obj):
        profile = obj.user.profile
        return PostUserSerializer(profile).data 
    
    def get_timestamp(self,obj):
        return obj.timestamp.strftime('%-d / %b %Y')