from typing import Any
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import Blog
from .serializers import BlogSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404


class CbvApiUser(APIView):
    permission_classes: list[Any] = [AllowAny,]
    def get(self,request):
         blogs = Blog.objects.all()
         result = BlogSerializer(blogs, many=True)
         return Response(result.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogDetailView(APIView):
    permission_classes: list[Any] = [AllowAny]

    def get_object(self, pk):
        return get_object_or_404(Blog, pk=pk)

    def get(self, request, pk):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,pk):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        blog = self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








