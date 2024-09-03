from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import ArticleViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]