from rest_framework import serializers

from .models import Reply,Tweet


class ReplySerializer(serializers.ModelSerializer):

    class Meta:
        model=Reply
        fields="__all__"


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = "__all__"

