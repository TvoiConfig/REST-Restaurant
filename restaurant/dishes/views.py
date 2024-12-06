from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from common.utils import forbidden_response
from database.models import Dishes
from dishes.serializers import DishesSerializer
from rest_framework import status, viewsets


class DishesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        name = request.query_params.get('name')
        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')

        dishes = Dishes.objects.all()

        if name:
            dishes = dishes.filter(name__icontains=name)
        if min_price:
            dishes = dishes.filter(price__gte=min_price)
        if max_price:
            dishes = dishes.filter(price__lte=max_price)

        serializer = DishesSerializer(dishes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        if not request.user.is_staff:
            return forbidden_response()
        serializer = DishesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        if not request.user.is_staff:
            return forbidden_response()

        try:
            dishes = Dishes.objects.get(pk=pk)
            dishes.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Dishes.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

