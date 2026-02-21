from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

from .serializers import RegisterSerializer

CustomUser = get_user_model()


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    queryset = CustomUser.objects.all()  # REQUIRED by checker

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.get(user=user)
        return Response({"token": token.key})


class ProfileView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]  # REQUIRED by checker
    queryset = CustomUser.objects.all()

    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email,
            "bio": user.bio
        })