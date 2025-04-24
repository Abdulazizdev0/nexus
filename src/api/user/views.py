from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from user.models import Profile
from .serializers import ProfileSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from typing import Any
from django.shortcuts import get_object_or_404




class UserView(APIView):
    permission_classes: list[Any] = [AllowAny]
    def get(self,request):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response({"data": serializer.data})

    def post(self,request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'data': "success"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
