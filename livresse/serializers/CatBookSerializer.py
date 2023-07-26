from rest_framework import serializers
from livresse.models import Category, CatBook

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CatBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatBook
        depth=1
        fields = '__all__'