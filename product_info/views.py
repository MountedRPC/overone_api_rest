from .models import Products
from rest_framework import viewsets
from rest_framework import permissions
from product_info.serializers import ProductsSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Products.objects.all().order_by('id')
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAuthenticated]
