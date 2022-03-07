from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (FavoriteApiView, RecipeViewSet,
                    ShoppingView, IngredientView)

router = DefaultRouter()
router.register('recipes', RecipeViewSet)
router.register(r'ingredients', IngredientView, basename='ingredients')

urlpatterns = [
    path('', include(router.urls)),
    path('recipes/<int:favorite_id>/favorite/', FavoriteApiView.as_view()),
    path('recipes/<int:recipe_id>/shopping_cart/', ShoppingView.as_view()),
]
