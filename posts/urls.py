from django.urls import path,include
from rest_framework import routers

from . import views

router=routers.DefaultRouter()

router.register('tweet',views.TweetViewSet,basename='tweet')
router.register('reaction_type',views.ReactionTypeViewSet)

urlpatterns=[
    path('', include(router.urls)),
    # path('tweet/<int:tweet_id>/reply/', views.ReplyViewSet.as_view({'post': 'create'}),name='create-reply'),
    # path('tweet/<int:tweet_id>/reply/<int:pk>/', views.ReplyViewSet.as_view({'get': 'retrieve'}), name='retrieve-reply'),

    path('tweet/<int:tweet_id>/reply/<int:pk>/', views.ReplyRetrieveUpdateDestroyAPIView.as_view(),name='reply-detail'),
    path('tweet/<int:tweet_id>/reply/', views.ReplyListCreateAPIView.as_view(),name='reply-list-create'),
    path('reply/<int:reply_id>/reaction/',views.ReplyReactionCreateAPIView.as_view())

]
