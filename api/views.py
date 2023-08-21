from rest_framework import generics
from book.models import Book
from .serializers import BookSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, BasePermission, IsAdminUser, DjangoModelPermissions


class BookUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class BookList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.postobjects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView, BookUserWritePermission):
    permission_classes = [BookUserWritePermission]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


""" Concrete View Classes
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""