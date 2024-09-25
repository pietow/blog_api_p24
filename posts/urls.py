from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path("v1/<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("v1/", PostList.as_view(), name="post_list"),
]