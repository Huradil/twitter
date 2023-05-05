from rest_framework import generics
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import TweetSerializer,ReplySerializer
from .models import Tweet,Reply


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer