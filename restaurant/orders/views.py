from tkinter.font import names

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from database.models import Dishes
from orders.serializers import DishesSerializer
from rest_framework import status


class DishesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
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

    def post(self, request):
        if not request.user.is_staff:
            return Response({"error": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
        serializer = DishesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Dishes add successful!"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if not request.user.is_staff:
            return Response({"error": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
        try:
            dish = Dishes.objects.get(pk=pk)
            dish.delete()
            return Response({"message": "Dish deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
        except Dishes.DoesNotExist:
            return Response({"error": "Dish does not exist!"}, status=status.HTTP_404_NOT_FOUND)




