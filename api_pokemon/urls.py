'''
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('core.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls'))
]
'''
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/v1/', include('core.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#    urlpatterns += static(settings.MEDIA_URL_2, document_root=settings.MEDIA_ROOT_2)
