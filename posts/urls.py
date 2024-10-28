<<<<<<< HEAD
# posts/urls.py
from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [ 
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"), 
    path("", PostList.as_view(), name="post_list"), 
]
=======
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, UserViewSet

router = SimpleRouter()
router.register("posts", PostViewSet)
router.register("users", UserViewSet, basename="users")

urlpatterns = router.urls
>>>>>>> PREP
