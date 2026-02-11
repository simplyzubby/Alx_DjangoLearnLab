from re import search
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from .views import (
    CommentDeleteView,
    CommentUpdateView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostsByTagView,
    SearchResultsView,
)

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('posts/<int:pk>/comments/new/', views.add_comment, name='add-comment'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('login/', auth_views.LoginView.as_view(
        template_name='blog/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        template_name='blog/logout.html'), name='logout'),
     path("comment/<int:pk>/update/", "post/<int:pk>/comments/new/", "comment/<int:pk>/delete/")

    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('tags/<str:tag_name>/', PostsByTagView.as_view(), name='posts-by-tag'),
    path('search/', SearchResultsView.as_view(), name='search'),
     path('search/', search, name='search'),
     path("post/<int:pk>/delete/", "post/<int:pk>/update/", "post/new/")
       path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='posts_by_tag'),  # <-- here
     
]