from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.HomePosts.as_view(), name = 'index'),
    path('category/<str:slug>/', views.PostsByCategory.as_view(), name='posts_by_category'),
    path('post/<str:slug>/', views.PostDetail.as_view(), name='post'),
    path('tag/<str:slug>/', views.PostsWithTag.as_view(), name='posts_with_tags'),
    path('search/', views.Search.as_view(), name='search'),
]