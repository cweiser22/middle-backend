from rest_framework import routers
from .apis import *

router = routers.SimpleRouter()

router.register(r'articles', ArticleViewSet, basename='articles')

urlpatterns = router.urls
