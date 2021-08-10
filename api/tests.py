from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from api.models import Restaurant

client = APIClient()
class TestRandomRestaurantView(TestCase):
    def setUp(self) -> None:
        for restaurant_id in range(5):
            Restaurant.objects.create(name=f"Restaurant{restaurant_id}")
    
    def test_get_random_restaurant(self):
        response = client.get(reverse("restaurants-random"))
        response_item = response.json()
        is_restaurant_available = Restaurant.objects.filter(id=response_item["id"]).exists()
        self.assertTrue(is_restaurant_available, "restaurant with ID from response is not availabe in test queryset")
