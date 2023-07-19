from rest_framework import serializers
from livresse.models import Category, CatBook

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CatBookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CatBook
        fields = '__all__'