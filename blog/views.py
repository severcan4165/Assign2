from django.shortcuts import render
from .models import Post
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .pagination import CustomPageNumberPagination

# Create your views here.

class PostMVS(ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticated]
    pagination_class=CustomPageNumberPagination