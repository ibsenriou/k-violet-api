from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from src.core.views.view_custom_user import CustomUserDetailView

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('', include('src.core.template_core_urls')),

    # Place this before the default auth urls, so that the custom one is used
    path('api/auth/user/', CustomUserDetailView.as_view(), name='user-detail'),

    path('api/core/', include('src.core.urls')),


    # Open API 3 schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))


admin.site.site_header = 'K-Violet™ API'
admin.site.site_title = 'K-Violet™ API'
admin.site.index_title = 'K-Violet™ API'
