from .views import AuthorViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'all', AuthorViewset)

urlpatterns = router.urls
