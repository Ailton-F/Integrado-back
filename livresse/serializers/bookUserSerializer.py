from livresse.models import Buy, Desire, PutBook
from rest_framework import serializers

class BuySerializer(serializers.ModelSerializer):
    class Meta:
        model = Buy
        fields = '__all__'

class DesireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desire
        fields = '__all__'
        
class PutBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = PutBook
        fields = '__all__'