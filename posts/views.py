from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly

class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        print('perform create')
        serializer.save(author=self.request.user)

    def get_queryset(self):
        print(self.request.user.is_superuser)
        if self.request.user.is_superuser:
            return Post.objects.all()
        return Post.objects.filter(author=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer