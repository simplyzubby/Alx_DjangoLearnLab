from rest_framework.routers import DefaultRouter
from .views import PostViewSet
from django.urls import path
from .views import like_post, unlike_post, FeedView

urlpatterns = [
    path('posts/<int:pk>/like/', like_post),
    path('posts/<int:pk>/unlike/', unlike_post),
    path('feed/', FeedView.as_view()),
]

router = DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = router.urls