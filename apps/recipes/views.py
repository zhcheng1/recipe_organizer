from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
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


class AddReview(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class UpdateReview(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


@api_view(['Get', 'Post'])
def SendEmail(request):
    subject = request.DATA['subject']
    message = request.DATA['message']
    from_email = request.DATA['from_email']
    if subject and message and from_email:
        try:
            send_mail(subject, message, '', [from_email, 'czqapply@gmail.com'])
        except BadHeaderError:
            return Response('Invalid header found.')
        return Response('Message Received!')
    else:
        return Response('Make sure all fields are entered and valid.')