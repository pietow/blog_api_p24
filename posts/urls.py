from django.urls import path
from .views import PostList, PostDetail, UserList, UserDetail

urlpatterns = [
    path("v1/<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("v1/", PostList.as_view(), name="post_list"),
    path("v1/users/<int:pk>/", UserDetail.as_view(), name="user_detail"),
    path("v1/users/", UserList.as_view(), name="User_list"),
]