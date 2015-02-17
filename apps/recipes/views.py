from django.shortcuts import render
from rest_framework import generics
from serializers import *
from rest_framework.decorators import api_view


class RecipeList(generics.ListAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


# class AddRecipe(generics.CreateAPIView):
#     serializer_class = RecipeSerializer
#     queryset = Recipe.objects.all()


@api_view(['GET', 'POST'])
def AddRecipe(request):
    file = request.DATA
    if file:
        print "oo"
    else:
        print "what"


class IngredientList(generics.ListAPIView):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()


class AddReview(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class UpdateReview(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()