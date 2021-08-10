import random

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action

from api.serializers import RestaurantSerializer
from api.models import Restaurant

class RestaurantCRUDViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    @action(methods=["get"], detail=False)  # this adds additional route besides those created by ViewSet
    def random(self, request):
        restaurants = list(self.queryset)
        random_restaurant = random.choice(restaurants)
        serialized_restaurant = self.serializer_class(random_restaurant)
        return Response(serialized_restaurant.data)