from rest_framework import viewsets, permissions, pagination
from .serializers import *
from .models import *


# permissions for the article viewset, doesnt allow updating or deleting an article that the user doesn't own
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.author == request.user


# this viewset handles everything related to articles
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer

    #anonympous users can still read
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly]

    # paginate
    pagination_class = pagination.PageNumberPagination

    def get_queryset(self):
        queryset = Article.objects.all()
        # if category is present in url, filter
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset

    def perform_create(self, serializer):
        # adds author data
        serializer.save(author=self.request.user)