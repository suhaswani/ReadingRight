from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from .serializers import PostSerializer
from rest_framework import permissions


class PostList(ListCreateAPIView):

    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(userid=self.request.user)

    def get_queryset(self):
        return Post.objects.filter(userid=self.request.user)


class PostDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Post.objects.filter(userid=self.request.user)
