from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewset, BooksViewset, BookList
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'authors', AuthorViewset, basename='AuthorView')
router.register(r'books', BooksViewset, basename='BooksView')

urlpatterns = [
    path('', include(router.urls)),
    path('booklist/', BookList.as_view(), name = 'book_list'),
    #jwt endpoints
    path('token/', TokenObtainPairView.as_view(), name = 'token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh')
]
