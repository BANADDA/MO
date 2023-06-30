from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.documentation import include_docs_urls

from photos.views import PhotoViewSet

router = routers.DefaultRouter()
router.register('photos', PhotoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),  # Add authentication URLs
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Add token authentication URL
    path('docs/', include_docs_urls(title='Photo API')),  # Add API documentation URL
]
