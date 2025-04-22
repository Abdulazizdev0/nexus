from user.models import User,Profile
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfileSerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated



@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def get_list_user(request):
    if request.method == "GET":
        profile = Profile.objects.all()
        result = ProfileSerializer(profile,many=True)
        print(result.data)
        return Response({"data":result.data})

    elif request.method == "POST":
        if not request.user.is_authenticated:
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = ProfileSerializer(data=request.data)
        print(serializer,serializer.is_valid())
        if serializer.is_valid():
            result = serializer.save(user=request.user)
            print(result)
            return Response({'data':"success"},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)