from rest_framework.routers import SimpleRouter
from .views import PostViewSet, UserViewSet

router = SimpleRouter()
router.register("posts", PostViewSet)
router.register("users", UserViewSet, basename="users")

urlpatterns = router.urls