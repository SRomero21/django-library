from .views import BookViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'all', BookViewset)

urlpatterns = router.urls

