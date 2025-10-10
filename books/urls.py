from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewset, BooksViewset
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'authorview', AuthorViewset, basename='AuthorView')
router.register(r'booksview', BooksViewset, basename='BooksView')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name = 'token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh')
]
