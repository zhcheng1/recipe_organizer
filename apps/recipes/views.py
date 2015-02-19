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


class AddRecipe(generics.CreateAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

# @api_view(['Get', 'Post'])
# def AddRecipe(request):
#     data = request.DATA
#     ingredient_list = request.DATA['ingredients']
#     ingredients = data.pop('ingredients')
#     ingredient_list = [e for e in ingredient_list.split(',')]
#     data['ingredients'] = ingredient_list
#     serializer = RecipeSerializer(data=data)
#     print serializer


class AddReview(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class UpdateReview(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()