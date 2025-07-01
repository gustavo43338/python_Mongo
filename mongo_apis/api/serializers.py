from rest_framework import serializers
from .models import Halo

class HaloSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    nombre = serializers.CharField()
    marca = serializers.CharField()
    stock = serializers.IntegerField()
    precio = serializers.CharField()
    cducidad = serializers.DateTimeField()
    lote = serializers.DateTimeField()

    def create(self, validated_data):
        halo = Halo(**validated_data)
        halo.save()
        return halo

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
