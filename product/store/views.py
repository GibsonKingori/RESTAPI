from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializer import ProductSerializer


#Product View
@api_view(['GET'])
def getProduct (response):
    product = Product.objects.all()
    Pdata = ProductSerializer(product, many=True).data
   if Pdata.is_valid():
       return Response(Pdata, status=status.HTTP_200_OK)
    return Response(Pdata, status=status.HTTP_400_BAD_REQUEST)