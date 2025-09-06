from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('admin/', admin.site.urls),
    path('blog_app/', include("blog_app.urls")),
    path('auth', include("auth_app.urls")),
    path('api-auth/', include('rest_framework.urls')),

    # JWT Authentication endpoints.
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # OAuth2 endpoints (using django-oauth-toolkit).
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
