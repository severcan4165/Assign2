from django.urls import path, include
from rest_framework import routers
from .views import PostMVS

router = routers.DefaultRouter()
router.register("blog",PostMVS)

urlpatterns = [
    path("", include(router.urls)),
    



]