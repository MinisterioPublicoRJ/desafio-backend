from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from desafio.models import LocalRegistrado
from desafio.serializers import LocalRegistradoSerializer


class LocalRegistradoView(generics.ListCreateAPIView):
    queryset = LocalRegistrado.objects.all()
    serializer_class = LocalRegistradoSerializer


# Implemente o serviço requerido aqui
class PontosProximosView(APIView):

    def get(self, request, *args, **kwargs):
        return Response("Pontos próximos!")

    # Pergunta 1:
    #
    #
    #
