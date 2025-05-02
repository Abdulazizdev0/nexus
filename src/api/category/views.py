from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySerializer
from category.models import Category
from django.http import HttpResponse
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.routers import DefaultRouter






@api_view(['GET','POST'])
def get_list_ctg(request):
    if request.method == "GET":
        categories = Category.objects.all()
        result = CategorySerializer(categories,many=True)
        print(result.data)
        return Response({"data":result.data})

    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        print(serializer,serializer.is_valid())
        if serializer.is_valid():
            result = serializer.save()
            print(result)
            return Response({'data':"success"},status=status.HTTP_201_CREATED)



@api_view(["GET","PUT","DELETE"])
def detail_ctg(request,pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({"error":"could not found"})

    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CategorySerializer(category,data=request.data)
        print(serializer.is_valid(),serializer)
        if serializer.is_valid():
            serializer.save()
            print(serializer)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({"error":"could not edit"},status=status.HTTP_400_BAD_REQUEST)


    elif request.method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

