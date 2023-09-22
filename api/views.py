from rest_framework import permissions, generics, status
from book.models import Book
from .serializers import BookSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework import filters
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

# Permision author
class BookUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


# Display Posts

class BookList(generics.ListAPIView):

    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookDetail(generics.RetrieveAPIView):

    serializer_class = BookSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Book, slug=item)


# Post Search

class BookListDetailfilter(generics.ListAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    # '^' Starts-with search.
    # '=' Exact matches.
    search_fields = ['^slug']


# Post Admin

class CreateBook(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminBookDetail(generics.RetrieveAPIView):
    permission_classes = [BookUserWritePermission]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class EditBook(generics.UpdateAPIView, BookUserWritePermission):
    permission_classes = [BookUserWritePermission]
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class DeleteBook(generics.RetrieveDestroyAPIView):
    permission_classes = [BookUserWritePermission]
    serializer_class = BookSerializer
    queryset = Book.objects.all()
