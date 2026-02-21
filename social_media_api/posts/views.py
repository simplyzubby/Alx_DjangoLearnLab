from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    # 👇 REQUIRED by ALX checker (exact string match)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    Like.objects.get_or_create(user=request.user, post_id=pk)
    return Response({"status": "liked"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    Like.objects.filter(user=request.user, post_id=pk).delete()
    return Response({"status": "unliked"})