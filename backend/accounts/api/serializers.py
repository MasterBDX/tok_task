from rest_framework import serializers


from django.conf import settings

from ..models import UserProfile

from urllib.parse import urljoin


class PostUserSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    slug = serializers.SerializerMethodField()

    class Meta:
        model= UserProfile
        fields = ['image','slug','username']
    
    def get_image(self,obj):
        base_url = getattr(settings,'BASE_URL','http://127.0.0.1:8000/')
        return urljoin(base_url,obj.get_avatar())
    
    def get_username(self,obj):
        return obj.user.username    
    
    def get_slug(self,obj):
        return obj.user.slug