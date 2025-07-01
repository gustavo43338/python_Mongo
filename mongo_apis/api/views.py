from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Halo
from .serializers import HaloSerializer
from mongoengine.errors import DoesNotExist

class HaloList(APIView):
    def get(self, request):
        halo = Halo.objects.all()
        serializer = HaloSerializer(halo, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HaloSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HaloDetail(APIView):
    def get(self, request, id):
        try:
            halo = Halo.objects.get(id=id)
            serializer = HaloSerializer(halo)
            return Response(serializer.data)
        except DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            halo = Halo.objects.get(id=id)
            serializer = HaloSerializer(halo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            halo = Halo.objects.get(id=id)
            halo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
