from django.urls import include, path
from rest_framework import routers
from photos.views import PhotoViewSet

router = routers.DefaultRouter()
router.register('photos', PhotoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
