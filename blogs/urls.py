from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import PostViewSet, BlogCommentViewSet, get_tinymce_api_key

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'comments', BlogCommentViewSet, basename='comments')

urlpatterns = router.urls + [
    path('get-tinymce-api-key/', get_tinymce_api_key, name='get_tinymce_api_key'),
]
