from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializer import ProductSerializer


#Product View
@api_view(['GET'])
def getProduct (request):
    product = Product.objects.all()
    pdata = ProductSerializer(product, many=True).data
    return Response(pdata)   
  