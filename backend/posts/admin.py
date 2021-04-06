from django.contrib import admin


from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','timestamp']

admin.site.register(Post)
