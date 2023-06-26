from django.urls import path
from .views import *

urlpatterns = [
    path('user/', UserModelViews.as_view(), name ='user-list'),
    path('user/<int:pk>/', UserModelDetailView.as_view(), name='respective-user') ,
    path('todo/', TodoModelViews.as_view(), name ='todo-list'),
    path('todo/<int:pk>/', TodoModelDetailView.as_view(), name='respective-todo'),
    path('category/', CategoryViews.as_view(), name ='category-list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='respective-category'),
    path('comment/', CommentViews.as_view(), name ='comment-list'),
    path('comment/<int:pk>/', CommentDetailView.as_view(), name='respective-comment'),
    path('tag/', TagModelViews.as_view(), name ='tag-list'),
    path('tag/<int:pk>/', TagModelDetailView.as_view(), name='respective-tag'), 
]
