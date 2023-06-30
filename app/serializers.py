from rest_framework import serializers
from .models import Local

class LocalSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=255)
    rua = serializers.CharField(max_length=255)
    numero = serializers.IntegerField()
    foto = serializers.URLField(allow_null=True)

    def create(self, validated_data):
        return Local.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.rua = validated_data.get('rua', instance.rua)
        instance.numero = validated_data.get('numero', instance.numero)
        instance.foto = validated_data.get('foto', instance.foto)
        return instance
