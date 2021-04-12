
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls',namespace='core')),
    
    path('api/posts/',include('posts.api.urls',namespace='api-posts')),
    path('api/accounts/',include('accounts.api.urls',namespace='api-accounts'))    
]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

