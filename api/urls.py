
from .views import BookList, BookDetail, BookListDetailfilter, CreateBook, EditBook, AdminBookDetail, DeleteBook
from django.urls import path

app_name = 'blog_api'

urlpatterns = [
    path('', BookList.as_view(), name='listpost'),
    path('post/<str:pk>/', BookDetail.as_view(), name='detailpost'),
    path('search/', BookListDetailfilter.as_view(), name='searchpost'),
    # Post Admin URLs
    path('admin/create/', CreateBook.as_view(), name='createpost'),
    path('admin/edit/postdetail/<int:pk>/', AdminBookDetail.as_view(), name='admindetailpost'),
    path('admin/edit/<int:pk>/', EditBook.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', DeleteBook.as_view(), name='deletepost'),
]