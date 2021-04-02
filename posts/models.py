from django.db import models

class Post(models.Model):
    content = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images',
                              blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:20]
