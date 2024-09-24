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
