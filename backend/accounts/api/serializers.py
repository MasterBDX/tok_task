from rest_framework import serializers

from ..models import UserProfile

class PostUserSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    slug = serializers.SerializerMethodField()

    class Meta:
        model= UserProfile
        fields = ['image','slug','username']
    
    def get_image(self,obj):
        return obj.get_avatar()
    
    def get_username(self,obj):
        return obj.user.username    
    
    def get_slug(self,obj):
        return obj.user.slug