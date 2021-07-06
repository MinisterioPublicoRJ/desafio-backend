from rest_framework import serializers

from desafio.models import LocalRegistrado


class LocalRegistradoSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=255)
    x = serializers.IntegerField(min_value=0)
    y = serializers.IntegerField(min_value=0)

    def create(self, validated_data):
        return LocalRegistrado.objects.create(**validated_data)
