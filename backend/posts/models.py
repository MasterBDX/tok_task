from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    content = models.CharField(_('Content'),max_length=255)
    image = models.ImageField(_('Image'),upload_to='images',
                              blank=True,null=True)
    user = models.ForeignKey(User ,verbose_name=_('User'),on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:20]
