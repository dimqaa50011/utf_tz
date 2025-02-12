from django.db.models import Prefetch
from rest_framework.generics import ListAPIView

from .serializers import FoodListSerializer, FoodSerializer
from .models import FoodCategory, Food


class FoodListAPIView(ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        return (
            FoodCategory.objects.filter(food__is_publish=True)
            .distinct()
            .prefetch_related(
                Prefetch("food", queryset=Food.objects.filter(is_publish=True))
            )
        )
