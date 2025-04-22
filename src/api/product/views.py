from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from product.models import Product
from django.http import HttpResponse
from rest_framework.decorators import api_view,permission_classes



@api_view(['GET','POST'])

def get_list_pr(request):
    if request.method == "GET":
        products = Product.objects.all()
        result = ProductSerializer(products,many=True)
        print(result.data)
        return Response({"data":result.data})

    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        print(serializer,serializer.is_valid())
        if serializer.is_valid():
            profile = request.user.profile
            serializer.save(user=profile)
            return Response({'data':"success"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)