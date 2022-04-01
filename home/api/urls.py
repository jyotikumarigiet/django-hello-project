from django.db import router
from django.urls.conf import include, path
from home.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('contapi', views.ContactViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls))
]
