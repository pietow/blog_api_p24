<<<<<<< HEAD
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    # author = serializers.CharField(source='author.username') # to specify the field name instead of the default id
    author = serializers.ReadOnlyField(source='author.username') # to specify the field name instead of the default id
    class Meta:
        fields = (
        "id",
        "author",
        "title",
        "body",
        "created_at",
        )
        model = Post
=======
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "username",
        )
        model = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "body",
            "created_at",
        )
        model = Post
>>>>>>> PREP
