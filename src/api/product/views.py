from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from product.models import Product
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from typing import Any
from django.shortcuts import get_object_or_404





class ProductView(APIView):
    permission_classes: list[Any] = [AllowAny]
    def get(self,request):
        products = Product.objects.all()
        result = ProductSerializer(products,many=True)
        print(result.data)
        return Response({"data":result.data})

    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        print(serializer,serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response({'data':"success"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):
    permission_classes: list[Any] = [AllowAny]
    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)

    def get(self, request,pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

