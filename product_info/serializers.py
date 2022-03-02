from .models import Products
from rest_framework import serializers


class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'image', 'name', 'description', 'price', 'id_user_id']
