from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Post, BlogComment
from .serializers import PostSerializer, BlogCommentSerializer
from rest_framework.pagination import PageNumberPagination
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


class CustomPagination(PageNumberPagination):
    """Custom pagination with 3 items per page."""
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10


class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing post instances.
    """
    queryset = Post.objects.all().order_by('-timeStamp')  # Sort by latest to oldest
    serializer_class = PostSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        """
        Optionally restricts the returned posts to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Post.objects.all().order_by('-timeStamp')
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(author__username=username)
        return queryset

    @action(detail=True, methods=['GET'])
    def comments(self, request, pk=None):
        """Get all comments for a specific post."""
        post = self.get_object()
        comments = BlogComment.objects.filter(post=post, parent=None)
        serializer = BlogCommentSerializer(comments, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def increment_views(self, request, pk=None):
        """Increment views for a specific post."""
        post = self.get_object()
        Post.objects.filter(pk=post.pk).update(views=F('views') + 1)
        post.refresh_from_db()
        return Response({"message": "Views incremented", "views": post.views})


class BlogCommentViewSet(viewsets.ModelViewSet):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer
    pagination_class = CustomPagination

    class CustomPagination(PageNumberPagination):
        """Custom pagination with 10 items per page."""
        page_size = 10
        page_size_query_param = 'page_size'
        max_page_size = 100


@login_required
def get_tinymce_api_key(request):
    return JsonResponse({'api_key': settings.TINYMCE_API_KEY})