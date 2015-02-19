from rest_framework import serializers
from models import *


class RecipeSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Recipe

    def create(self, validated_data):
        recipe = Recipe.objects.create(**validated_data)
        return recipe

    def get_reviews(self, obj):
        reviews = Review.objects.filter(recipe_id=obj.id)
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review

    def create(self, validated_data):
        return Review.objects.create(**validated_data)


