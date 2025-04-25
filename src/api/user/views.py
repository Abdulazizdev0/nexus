from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework import status
from user.models import Profile
from .serializers import ProfileSerializer
from rest_framework.permissions import AllowAny
from typing import Any
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework import mixins







# class BlogGenericApiView(GenericAPIView):
#     permission_classes: list[Any] = [AllowAny, ]
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#
#     def get(self,request):
#         profil = self.get_queryset()
#         serializer = self.get_serializer(profil,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#
#     def post(self,request):
#         serializer = self.get_serializer(data=request.data)
#         print(serializer)
#         print(serializer.is_valid())
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         else:
#             return Response({'data':'invalid'},status=status.HTTP_400_BAD_REQUEST)



class ProfileGenericApiView(mixins.ListModelMixin,mixins.CreateModelMixin,GenericAPIView):
    permission_classes: list[Any] = [AllowAny, ]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


    # def put(self,request,*args,**kwargs):
    #     return self.update(request, *args, **kwargs)

class ProfileGenericApiMixinsdetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,GenericAPIView,):
    permission_classes: list[Any] = [AllowAny, ]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'pk'


    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)



class ProfileGenericApidetail(GenericAPIView,):
    permission_classes: list[Any] = [AllowAny, ]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer



    def get(self,request,*args,**kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def put(self,request,*args,**kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance,data=request.data)
        if serializer.is_valid():
            print(serializer.is_valid)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,*args,**kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
















