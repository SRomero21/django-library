from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register("users", UserViewSet)
#router.register("author", AuthorViewSet)
#router.register("title", TitleViewSet)
#router.register("pubdate", PubDateViewSet)
#router.register("sujeto", SubjectViewSet)
#router.register("category", CategoryViewSet)

urlpatterns = router.urls 