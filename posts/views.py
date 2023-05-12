from datetime import timedelta, datetime
from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination

from .models import Tweet, Reply, ReactionType, ReplyReaction
from .permissions import IsAuthorOrIsAuthenticated, IsAdminOrReadOnly
from .serializers import TweetSerializer, ReplySerializer, ReactionSerializer, ReactionTypeSerializer, \
    ReplyReactionSerializer
from . import paginations


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    authentication_classes = [TokenAuthentication,BasicAuthentication,SessionAuthentication]
    permission_classes = [IsAuthorOrIsAuthenticated,]
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    # pagination_class = paginations.TweetNumberPagination
    pagination_class = LimitOffsetPagination
    search_fields = ['text','profile__user__username']
    ordering_fields = ['updated_at', 'profile__user_id']

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)

    @action(methods=['POST'],detail=True,serializer_class=ReactionSerializer,
            permission_classes=[permissions.IsAuthenticated],
            authentication_classes=[TokenAuthentication,BasicAuthentication,SessionAuthentication])
    def reaction(self,request,pk=None):
        serializer=ReactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                profile=self.request.user.profile,
                tweet=self.get_object()
            )
            return Response(serializer.data)
        return Response(serializer.errors,status=400)

    @action(methods=['GET'],detail=False,name='last_5_days_tweet')
    def get_tweet(self,request,pk=None):
        five_days_ago = datetime.now().date()-timedelta(days=5)
        tweets=Tweet.objects.filter(created_add__gte=five_days_ago)
        serializer=TweetSerializer(instance=tweets,many=True)
        return Response(serializer.data)


class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    authentication_classes = [TokenAuthentication,BasicAuthentication,SessionAuthentication]
    permission_classes = [IsAuthorOrIsAuthenticated,]
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    pagination_class = LimitOffsetPagination
    search_fields = ['text', ]
    ordering_fields = ['updated_at', ]


class ReplyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [IsAuthorOrIsAuthenticated]
    authentication_classes = [TokenAuthentication,BasicAuthentication,SessionAuthentication]

    def get_queryset(self):
        return super().get_queryset().filter(tweet_id=self.kwargs['tweet_id'])


class ReplyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [IsAuthorOrIsAuthenticated]
    authentication_classes = [TokenAuthentication,BasicAuthentication,SessionAuthentication]

    def get_queryset(self):
        return super().get_queryset().filter(tweet_id=self.kwargs['tweet_id'])

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)


class ReactionTypeViewSet(viewsets.ModelViewSet):
    queryset = ReactionType.objects.all()
    serializer_class = ReactionTypeSerializer
    authentication_classes = [TokenAuthentication,BasicAuthentication,SessionAuthentication]
    permission_classes = [IsAdminOrReadOnly]


# class ReactionCreateAPIView(generics.CreateAPIView):
#     queryset = Reaction.objects.all()
#     serializer_class = ReactionSerializer
#     authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
#
#     def perform_create(self, serializer):
#         serializer.save(
#             profile=self.request.user.profile,
#             tweet_id=self.kwargs['tweet_id']
#         )

class ReplyReactionCreateAPIView(generics.CreateAPIView):
    queryset = ReplyReaction.objects.all()
    serializer_class = ReplyReactionSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(
            profile=self.request.user.profile,
            reply=get_object_or_404(Reply,pk=self.kwargs['reply_id'])
        )
